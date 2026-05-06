# 🎹 AI Piano Transcriber (Browser-based) 

這是一個基於 AI 技術的自動轉譜工具，能夠將音訊檔案（MP3/WAV）轉換為數位 MIDI 樂譜。本專案利用 **WebAssembly (WASM)** 技術，讓複雜的機器學習模型直接在您的瀏覽器中運行，無需任何後端伺服器。

## 🚀 線上操作網址
[點此開啟 AI 轉譜工具](https://你的GitHub帳號.github.io/你的倉庫名稱/)

---

## ✨ 核心特色

### 1. 隱私安全 (Private & Secure)
所有的音訊處理與 AI 辨識都在您的本機瀏覽器完成。音檔**不會被上傳**到任何伺服器，確保您的創作隱私。

### 2. 長音軌分段處理 (Chunking Pipeline)
針對超過 5 分鐘的長歌曲，系統會自動將其切割為數個 30 秒的片段進行辨識。


### 3. 主動記憶體回收 (Memory Optimization)
整合了 Python `gc` 模組，在每個片段處理完畢後立即回收記憶體。這解決了 WebAssembly 環境中常見的記憶體溢出（OOM）問題，讓處理 5 分鐘以上的歌曲變得穩定。


### 4. 鋼琴捲軸視覺化 (Piano Roll Visualization)
轉換完成後，網頁會自動生成動態鋼琴捲軸圖表，方便您在下載前預覽 AI 的辨識結果。

---

## 🛠️ 技術棧 (Tech Stack)

- **AI 模型**: [Spotify Basic Pitch](https://github.com/spotify/basic-pitch) (ICASSP 2022)
- **前端框架**: [Streamlit](https://streamlit.io/) via [Stlite](https://github.com/whitphx/stlite) (WASM)
- **音訊處理**: Librosa, Pretty MIDI
- **部署平台**: GitHub Pages

---

## 📖 使用指南

1. **上傳檔案**: 選擇您的 MP3 或 WAV 檔案（建議單一樂器如鋼琴、吉他的效果最佳）。
2. **開始解析**: 點擊「開始分段解析」。
3. **等待處理**: 
    - 首次執行時，瀏覽器需要下載約 60MB 的模型數據。
    - 處理 5 分鐘的歌曲約需 2-4 分鐘（取決於您的 CPU 效能）。
4. **下載 MIDI**: 解析完成後，下載 `.mid` 檔案。
5. **後續編輯**: 您可以將 MIDI 檔匯入 **MuseScore**、**Sibelius** 或 **GarageBand** 生成標準五線譜。

---

## ⚠️ 注意事項

- **硬體需求**: 由於 AI 模型在瀏覽器端運行，建議使用具備較佳 CPU 效能的電腦開啟，並關閉其他高耗能網頁。
- **準確度限制**: 目前模型對純鋼琴或單一樂器的辨識度較高；若背景有重低音或人聲，辨識效果會受到干擾。

---

## 👤 作者
**Peter Yen (顏伯聰)** 專注於 RAG 系統開發、LLM 應用與自動化工程。

