import requests
from config import API_KEY_YT
from exceptions import ChatIDNotFoundError


def get_liveChatID(streamer_data):
    """
    Obtém o ID do chat ao vivo de um vídeo no YouTube.

    Args:
        streamer_data (dict): Dicionário contendo a chave "videoId".

    Returns:
        dict: Novo dicionário contendo as informações originais mais o "liveChatId".

    Raises:
        ChatIDNotFoundError: Se nenhum chat ao vivo for encontrado ou ocorrer erro na requisição  

    """

    video_id = streamer_data['videoId']
    url = f"https://www.googleapis.com/youtube/v3/videos?part=liveStreamingDetails&id={video_id}&key={API_KEY_YT}"

    try:

        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        items = data.get("items")
        if items:
            live_chat_id = items[0]["liveStreamingDetails"]["activeLiveChatId"]
            return {**streamer_data, "liveChatId": live_chat_id}

        raise ChatIDNotFoundError(
            "❌ Nenhum chat ao vivo encontrado para este vídeo.")

    except requests.RequestException as ex:
        raise ChatIDNotFoundError(f"❌ Erro na requisição HTTP: {ex}")

    except (KeyError, IndexError) as ex:
        raise ChatIDNotFoundError(
            f"❌ Erro ao processar dados do YouTube: {ex}")
