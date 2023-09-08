import os 
from yt_dlp import YoutubeDL
import ffmpeg

path = r'C:\Users\Administrator\Desktop\store\ffmpegc\ppl\bin'
os.environ['PATH'] +=  '' if path in os.environ['PATH'] else ';' + path
option = {
    "outtmpl": r'C:\Users\Administrator\Desktop\%(title)s.%(ext)s',
    "format":'bestvideo+bestaudio/best'
}
ydl = YoutubeDL(option)
result = ydl.download(['https://www.youtube.com/watch?v=1fCKnAmiXtU'])