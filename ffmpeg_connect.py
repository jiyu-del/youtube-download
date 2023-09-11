import ffmpeg
import os

ffmpeg_path = r'C:\Users\Administrator\Desktop\ffmpegc\ppl\bin'
file_path = r"C:\Users\Administrator\Desktop\python_test"
audio_path = os.path.join(file_path,"audio1.mp3")
video_path = os.path.join(file_path,"video.mp4")
output_path = os.path.join(file_path,"finished_video.mp4")
os.environ['PATH'] +=  '' if ffmpeg_path in os.environ['PATH'] else ';' + ffmpeg_path
audio = ffmpeg.input(audio_path)
video = ffmpeg.input(video_path)
ffmpeg.output(audio, video, output_path).run(overwrite_output=True)
