import os
from config import FFMPEG_PATH, YT_DLP_PATH
from core.chat_listener import start_monitor_chat
from core.get_channelID_by_handle import get_channelID_by_handle
from core.get_videoID import get_videoID_by_channelID
from core.get_liveChatID import get_liveChatID
from core.live_recording import start_live_recording
from exceptions import ChannelIDNotFoundError, FFmpegNotFoundError, VideoIDNotFoundError, YTDLNotFoundError


def main():
    try:
        print("🔎 Buscando Channel ID...")
        data_streamer = get_channelID_by_handle()
        print(f"✅ Channel ID encontrado...")

        print("🎥 Verificando se há live ativa...")
        data_streamer = get_videoID_by_channelID(data_streamer)

        print("🔎 Buscando Live Chat ID...")
        data_streamer = get_liveChatID(data_streamer)
        print(f"✅ Live ativa detectada!...")

        print(f"✅ Live Chat ID encontrado")

        if not os.path.exists(FFMPEG_PATH):
            raise YTDLNotFoundError(
                message="yt-dlp não encontrado. Verifique o caminho!")

        if not os.path.exists(YT_DLP_PATH):
            raise FFmpegNotFoundError(
                message="ffmpeg não encontrado. Verifique o caminho!")

        start_live_recording(data_streamer)
        print("🚀 Iniciando o monitoramento do chat e gravação em backstage!")

        print("✅ Monitorando o chat... Pressione Ctrl + C para parar.")
        start_monitor_chat(data_streamer)

    except ChannelIDNotFoundError as ce:
        print(str(ce))
    except VideoIDNotFoundError as ve:
        print(str(ve))
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")


if __name__ == "__main__":
    main()
