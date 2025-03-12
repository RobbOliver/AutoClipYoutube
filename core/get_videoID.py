import requests
from config import API_KEY_YT
from exceptions import VideoIDNotFoundError


def get_videoID_by_channelID(data_streamer):
    """
    Obtém o Video ID de uma live ativa a partir do Channel ID no YouTube.

    Args:
        data_streamer (dict): Dicionário contendo a chave "ChannelID".

    Returns:
        dict: Novo dicionário contendo as informações originais mais o "videoId".

    Raises:
        VideoIDNotFoundError: Se nenhum vídeo ao vivo for encontrado ou ocorrer erro na requisição.
    """

    channel_id = data_streamer.get("ChannelID")
    if not channel_id:
        raise VideoIDNotFoundError(
            "❌ ChannelID não encontrado no dicionário fornecido.")

    url = (
        "https://www.googleapis.com/youtube/v3/search"
        f"?part=id&channelId={channel_id}&type=video&eventType=live&key={API_KEY_YT}"
    )

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        items = data.get("items")
        if items:
            video_id = items[0]["id"]["videoId"]
            return {**data_streamer, "videoId": video_id}

        raise VideoIDNotFoundError(
            "❌ Nenhuma live ativa encontrada para este canal.")

    except requests.RequestException as ex:
        raise VideoIDNotFoundError(f"❌ Erro na requisição HTTP: {ex}")

    except (KeyError, IndexError) as ex:
        raise VideoIDNotFoundError(
            f"❌ Erro ao processar dados do YouTube: {ex}")
