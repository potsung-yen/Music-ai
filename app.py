import streamlit as st
import io, librosa, gc, pandas as pd, altair as alt, pretty_midi, numpy as np
from basic_pitch.inference import predict
from basic_pitch import ICASSP_2022_MODEL_PATH

st.set_page_config(page_title="AI 鋼琴轉譜系統", layout="wide")

# 側邊欄日誌
st.sidebar.title("🛠 執行監控")
log_area = st.sidebar.empty()
log_list = []

def write_log(msg):
    log_list.insert(0, f"> {msg}")
    log_area.code("\n".join(log_list[:12]))

st.title("🎹 AI 全曲轉譜與動態預覽")
st.info("系統將自動分段處理長音軌並回收記憶體以維持穩定。")

uploaded_file = st.file_uploader("選擇音檔 (MP3/WAV)", type=["mp3", "wav"])

if uploaded_file:
    st.audio(uploaded_file)
    if st.button("🚀 開始全曲解析"):
        try:
            write_log("正在讀取音訊...")
            y_full, sr = librosa.load(io.BytesIO(uploaded_file.read()), sr=22050)
            duration = librosa.get_duration(y=y_full, sr=sr)
            
            chunk_size = 30
            num_chunks = int(np.ceil(duration / chunk_size))
            
            final_midi = pretty_midi.PrettyMIDI()
            piano = pretty_midi.Instrument(program=0)
            final_midi.instruments.append(piano)
            
            viz_data = []
            pbar = st.progress(0)
            status = st.empty()

            for i in range(num_chunks):
                t_start = i * chunk_size
                t_end = min((i + 1) * chunk_size, duration)
                status.warning(f"⚡ 處理中: {t_start}s - {t_end}s ({i+1}/{num_chunks})")
                write_log(f"解析段落 {i+1}...")

                y_chunk = y_full[int(t_start * sr):int(t_end * sr)]
                _, midi_chunk, note_events = predict(ICASSP_2022_MODEL_PATH, y_chunk)
                
                for inst in midi_chunk.instruments:
                    for note in inst.notes:
                        note.start += t_start
                        note.end += t_start
                        piano.notes.append(note)
                
                for n in note_events:
                    viz_data.append({'time': n[0]+t_start, 'pitch': n[2], 'velocity': n[3], 'end': n[1]+t_start})

                del y_chunk, midi_chunk
                gc.collect()
                pbar.progress((i + 1) / num_chunks)

            status.success("✅ 解析完成！")
            write_log("生成視覺化預覽...")
            
            df = pd.DataFrame(viz_data)
            chart = alt.Chart(df.head(2000)).mark_bar().encode(
                x=alt.X('time:Q', title='時間 (秒)'),
                x2='end:Q',
                y=alt.Y('pitch:Q', scale=alt.Scale(zero=False), title='琴鍵位置'),
                color=alt.Color('velocity:Q', scale=alt.Scale(scheme='viridis')),
            ).properties(height=400).interactive()
            
            st.altair_chart(chart, use_container_width=True)

            midi_io = io.BytesIO()
            final_midi.write(midi_io)
            st.download_button("📥 下載 MIDI 檔案", midi_io.getvalue(), "output.mid")
            write_log("任務結束。")

        except Exception as e:
            st.error(f"錯誤: {e}")
            write_log(f"錯誤: {e}")
