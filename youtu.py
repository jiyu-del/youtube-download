import os 
from yt_dlp import YoutubeDL
import ffmpeg

path = r'C:\Users\Administrator\Desktop\store\ffmpegc\ppl\bin'
#Replace with your ffmpeg address
os.environ['PATH'] +=  '' if path in os.environ['PATH'] else ';' + path
option = {
    # Replace "outtmpl" with the address where you want to save the output file
    "outtmpl": r'C:\Users\Administrator\Desktop\%(title)s.%(ext)s',
    "format":'bestvideo+bestaudio/best'
}
ydl = YoutubeDL(option)
#Use URL that you want to download instead of "https://www.youtube.com/watch?v=1fCKnAmiXtU"
result = ydl.download(['https://www.youtube.com/watch?v=1fCKnAmiXtU'])
