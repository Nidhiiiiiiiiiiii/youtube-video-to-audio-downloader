# 🎵 YouTube to MP3 Downloader

A full-stack web application that lets users convert **YouTube videos to downloadable MP3 audio** files. Built with **React** frontend and **FastAPI** backend using `yt-dlp` and `ffmpeg`.

---

## 🚀 Features

- 🔗 Paste any YouTube video URL
- 🎧 Convert the video to high-quality MP3 audio
- 💾 Instantly download the converted audio
- ⚡ Fast processing using `yt-dlp` and `ffmpeg`
- 🧰 Simple UI built with React

---

## 🖥️ Tech Stack

| Layer     | Tech Used             |
|-----------|-----------------------|
| Frontend  | React, Axios, Tailwind CSS |
| Backend   | FastAPI, yt-dlp, ffmpeg |
| Language  | Python, JavaScript    |

---

## 📂 Project Structure

youtube-video-to-audio/
├── backend/
│ ├── main.py # FastAPI server
│ └── requirements.txt # Python dependencies
├── frontend/
│ ├── src/
│ │ ├── App.jsx # Main React component
│ │ └── ...
│ └── package.json # React dependencies

yaml
Copy
Edit

---

## 🔧 Setup Instructions

### 1️⃣ Backend (FastAPI + yt-dlp + ffmpeg)

#### ⬇ Install dependencies
```bash
cd backend
pip install -r requirements.txt
```
⚙ Ensure ffmpeg is installed and accessible
Download from https://www.gyan.dev/ffmpeg/builds/
Extract and add the /bin folder path to your system's Environment Variables

To verify:

```bash
ffmpeg -version
ffprobe -version
```
🚀 Start FastAPI server
```bash
uvicorn main:app --reload
```
2️⃣ Frontend (React)
⬇ Install dependencies
```bash
cd frontend
npm install
```
🚀 Start React app
```bash
npm run dev
```
Frontend will run on:
http://localhost:5173

Backend will run on:
http://localhost:8000

🔄 How It Works
User pastes a YouTube link in the input field.

Frontend sends a POST request to the FastAPI server.

Backend uses yt-dlp to download and ffmpeg to convert the video to MP3.

Converted MP3 file is sent back for download.


✅ To-Do
 Build UI with React

 Integrate FastAPI backend

 Add audio conversion logic

 🌐 Deploy on Render or Vercel

 🎯 Add download history/log

 🔐 Add authentication (optional)

💡 Credits
yt-dlp – YouTube downloading

ffmpeg – Media conversion

FastAPI – Python web framework

React – Frontend UI
