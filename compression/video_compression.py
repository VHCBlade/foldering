import os
import subprocess

input_dir = "input/"
output_dir = "output/"


def compress_video(input_file_path, output_file_path, crf=23):
    ffmpeg_cmd = f'ffmpeg -i "{input_file_path}" -c:v libx264 -crf {crf} -preset veryslow -vf scale=-1:720 -c:a copy "{output_file_path}"'

    subprocess.call(ffmpeg_cmd, shell=True)


def compress_videos_in_directory(input_dir, output_dir):
    video_files = [f for f in os.listdir(input_dir) if os.path.isfile(os.path.join(
        input_dir, f)) and f.lower().endswith(('.mp4', '.avi', '.mov', '.mkv', '.flv', '.wmv', '.webm'))]

    for video_file in video_files:
        input_path = os.path.join(input_dir, video_file)
        output_path = os.path.join(output_dir, video_file)
        compress_video(input_path, output_path)


compress_videos_in_directory(input_dir, output_dir)
