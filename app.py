import streamlit as st
import io, librosa, gc, pandas as pd, altair as alt, pretty_midi, numpy as np
from basic_pitch.inference import predict
from basic_pitch import ICASSP_2022_MODEL_PATH

# --- 關鍵：關閉 HTML 的載入畫面 ---
st.markdown("""
    <script>
        window.parent.document.getElementById('loader').style.display = 'none';
    </script>
""", unsafe_allow_html=True)

st.set_page_config(page_title="AI 鋼琴轉譜系統", layout="wide")

# (以下接您原本的 app.py 邏輯...)
st.title("🎹 AI 全曲轉譜與動態預覽")
# ... 其餘代碼不變 ...
