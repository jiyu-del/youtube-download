import pytube
import ffmpeg
import os
from moviepy.editor import *

# Youtube video URL
link = "https://www.youtube.com/watch?v=gwLsC4rKdyw"
yt = pytube.YouTube(link)

print("Title:", yt.title)
print("Author:", yt.author)
print("Published date:", yt.publish_date.strftime("%Y-%m-%d"))
print("Number of views:", yt.views)
print("Length of video:", yt.length, "seconds")

#下载方式1：下载音频和视频总体质量最高流，默认为720p
#yt.streams.get_highest_resolution().download()
#print("Video successfullly downloaded from", link)


#下载方式2：分开下载最高质量视频和音频，然后混合，方式有两种：ffmpeg +moviepy
#download audio only
yt.streams.filter(only_audio=True).first().download(filename="audio.mp3")

#download video only
yt.streams.filter(res="1080p", progressive=False).first().download(filename="video.mp4")

#---(1):------ffmpeg方式------
#指定ffmpeg文件路径，替代方案是将ffmpeg路径添加到环境变量中
ffmpeg_path = r'C:\Users\Administrator\Desktop\ffmpegc\ppl\bin'
os.environ['PATH'] +=  '' if ffmpeg_path in os.environ['PATH'] else ';' + ffmpeg_path

audio = ffmpeg.input("audio.mp3")
video = ffmpeg.input("video.mp4")
ffmpeg.output(audio, video, "finished_video.mp4").run(overwrite_output=True)

#---(2):------moviepy方式------

# Create instances of VideoFileClip and AudioFileClip
video_clip = VideoFileClip("video.mp4")
audio_clip = AudioFileClip("audio.mp3")

# Merge the audio and video clips
video_clip_with_audio = video_clip.set_audio(audio_clip)

# Write the merged video file to a new file
video_clip_with_audio.write_videofile("outfile.mp4")