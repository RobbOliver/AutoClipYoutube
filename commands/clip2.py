import datetime
import os
import subprocess

from config import FFMPEG_PATH


def run(user):
    # Nome do clipe com data/hora
    clip_name = f"clip_{datetime.datetime.utcnow().strftime('%Y-%m-%d_%H-%M-%S')}.mp4"

    # Salvar na área de trabalho
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", clip_name)

    # Comando FFmpeg para cortar últimos 60 segundos
    subprocess.run([
        FFMPEG_PATH,
        "-sseof", "-60",  # Pega últimos 60s
        "-i", "live_recording.mp4.part",  # Arquivo que está sendo gravado
        "-c", "copy",  # Sem re-encode (rápido)
        desktop_path
    ])

    print(f"✅ Clip criado: {desktop_path}")
