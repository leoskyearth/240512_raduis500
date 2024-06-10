# 유투브 url를 넣으면 MP3로 다운로드

import streamlit as st
import yt_dlp
import os

def download_audio(video_url):
    options = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'ffmpeg_location': r'C:\Users\m9938\OneDrive\바탕 화면\ffmpeg-2024-06-06-git-d55f5cba7b-full_build\bin'  # Adjust as necessary
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([video_url])

def main():
    st.title('YouTube Audio Downloader')
    video_url = st.text_input("Enter the YouTube video URL")
    if st.button('Download'):
        download_audio(video_url)
        st.success('Downloaded successfully!')

if __name__ == '__main__':
    main()
