# # from fastapi import FastAPI, Form
# # from fastapi.middleware.cors import CORSMiddleware
# # from fastapi.responses import FileResponse
# # import uuid
# # import os
# # import yt_dlp

# # app = FastAPI()

# # app.add_middleware(
# #     CORSMiddleware,
# #     allow_origins=["*"],  # set React URL in production
# #     allow_methods=["*"],
# #     allow_headers=["*"],
# # )

# # DOWNLOAD_DIR = "downloads"
# # os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# # @app.post("/download-audio/")
# # async def download_audio(youtube_url: str = Form(...)):
# #     file_id = str(uuid.uuid4())
# #     filename = os.path.join(DOWNLOAD_DIR, f"{file_id}.mp3")

# #     ydl_opts = {
# #         'format': 'bestaudio/best',
# #         'outtmpl': filename,
# #         'postprocessors': [{
# #             'key': 'FFmpegExtractAudio',
# #             'preferredcodec': 'mp3',
# #         }],
# #         'quiet': True,
# #     }

# #     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
# #         ydl.download([youtube_url])

# #     return {"file": f"http://localhost:8000/get-audio/{file_id}"}

# # @app.get("/get-audio/{file_id}")
# # async def get_audio(file_id: str):
# #     file_path = os.path.join(DOWNLOAD_DIR, f"{file_id}.mp3")
# #     return FileResponse(file_path, media_type='audio/mpeg', filename="audio.mp3")



# from fastapi import FastAPI, Request
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel
# import os
# import yt_dlp

# app = FastAPI()

# # Allow requests from frontend
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Replace with frontend URL in production
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Directory to store downloaded files
# DOWNLOAD_DIR = os.path.join(os.getcwd(), "downloads")
# os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# # Path to FFmpeg bin
# FFMPEG_PATH = r"C:\Users\Nidhi\Downloads\ffmpeg-7.1.1-essentials_build\ffmpeg-7.1.1-essentials_build\bin"

# class VideoUrl(BaseModel):
#     url: str

# @app.post("/download-audio/")
# async def download_audio(data: VideoUrl):
#     youtube_url = data.url

#     ydl_opts = {
#         'format': 'bestaudio/best',
#         'ffmpeg_location': FFMPEG_PATH,  # Explicitly tell yt-dlp where ffmpeg is
#         'outtmpl': os.path.join(DOWNLOAD_DIR, '%(title)s.%(ext)s'),
#         'postprocessors': [{
#             'key': 'FFmpegExtractAudio',
#             'preferredcodec': 'mp3',
#             'preferredquality': '192',
#         }],
#     }

#     try:
#         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#             info = ydl.extract_info(youtube_url, download=True)
#             filename = ydl.prepare_filename(info)
#             audio_file = os.path.splitext(filename)[0] + ".mp3"
#             return {"status": "success", "file": os.path.basename(audio_file)}
#     except Exception as e:
#         return {"status": "error", "message": str(e)}



from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import uuid
from yt_dlp import YoutubeDL

app = FastAPI()

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or specify ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Input model
class YouTubeURL(BaseModel):
    url: str

@app.post("/download-audio/")
async def download_audio(youtube_url: YouTubeURL):
    try:
        output_dir = "downloads"
        os.makedirs(output_dir, exist_ok=True)
        unique_filename = f"{uuid.uuid4()}.mp3"

        ydl_opts = {
            'format': 'bestaudio/best',
            'ffmpeg_location': r'C:\Users\Nidhi\Downloads\ffmpeg-7.1.1-essentials_build\ffmpeg-7.1.1-essentials_build\bin',  # ✅ Correct full path
            'outtmpl': os.path.join(output_dir, unique_filename),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_url.url])

        return {"message": "Audio downloaded successfully", "filename": unique_filename}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Download failed: {str(e)}")
