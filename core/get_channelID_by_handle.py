import requests
from config import API_KEY_YT, YOUTUBER_CHANNEL
from exceptions import ChannelIDNotFoundError


def get_channelID_by_handle():
    """
    Obtém o Channel ID a partir do Handle do YouTube.

    Returns:
        str: Channel ID se encontrado.

    Raises:
        ChannelIDNotFoundError: Se o canal não for encontrado ou ocorrer erro na requisição.
    """

    url = f"https://www.googleapis.com/youtube/v3/channels?part=id&forHandle={YOUTUBER_CHANNEL}&key={API_KEY_YT}"

    try:
        response = requests.get(url, timeout=10)  # To not get Locked
        response.raise_for_status()  # Rise Error if not 200 status code
        data = response.json()

        items = data.get("items")
        if items and len(items) > 0:
            return items[0]["id"]

        raise ChannelIDNotFoundError(
            "❌ No channels found for this handle.")

    except requests.RequestException as ex:
        raise ChannelIDNotFoundError(f"❌ HTTP request error: {ex}")

    except KeyError as ex:
        raise ChannelIDNotFoundError(f"❌ Error - ID was not found: {ex}")
