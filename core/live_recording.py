import os
import subprocess

from config import YT_DLP_PATH


def start_live_recording(data_streamer):

    video_url = f"https://www.youtube.com/watch?v={data_streamer['videoId']}"
    output_file = os.path.join(os.getcwd(), "live_recording.mp4")

    subprocess.Popen([
        YT_DLP_PATH,
        "-q",
        "--no-warnings",
        "-f", "best",
        "-o", output_file,
        video_url
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
