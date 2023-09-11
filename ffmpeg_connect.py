import ffmpeg
import os

------ffmpeg方式合并音频和视频------

#ffmpeg.exe 所在路径
ffmpeg_path = r'C:\Users\Administrator\Desktop\ffmpegc\ppl\bin'
#单独音频和视频文件所在路径
file_path = r"C:\Users\Administrator\Desktop\python_test"
#形成音频和视频路径
audio_path = os.path.join(file_path,"audio1.mp3")
video_path = os.path.join(file_path,"video.mp4")
output_path = os.path.join(file_path,"finished_video.mp4")
os.environ['PATH'] +=  '' if ffmpeg_path in os.environ['PATH'] else ';' + ffmpeg_path
#读取音频和视频路经
audio = ffmpeg.input(audio_path)
video = ffmpeg.input(video_path)
#ffmpeg方式合并音频和视频文件
ffmpeg.output(audio, video, output_path).run(overwrite_output=True)
