import requests
from config import API_KEY_YT, YOUTUBER_CHANNEL


def get_channelID_by_handle():
    """
    Obtém o Channel ID a partir do Handle do YouTube.

    Returns:
        str: Channel ID se encontrado.
        None: Se não encontrado ou ocorrer erro na requisição.
    """

    url = f"https://www.googleapis.com/youtube/v3/channels?part=id&forHandle={YOUTUBER_CHANNEL}&key={API_KEY_YT}"

    try:
        response = requests.get(url)
        response.raise_for_status() # Rise Error if not 200 status code
        data = response.json()

        items = data.get("items")
        if items and len(items) > 0:
            return items[0]["id"]
        else:
            return 

        if data["items"]:
            channelID = data["items"][0]["id"]
            return channelID
        else:
            return None
    except:
