import requests
import time


from config import API_KEY_YT


NEXT_PAGE_TOKEN = None


def get_chat_messages(streamer_data):
    global NEXT_PAGE_TOKEN
    live_chat_id = streamer_data["liveChatId"]

    url = f"https://www.googleapis.com/youtube/v3/liveChat/messages?liveChatId={live_chat_id}&part=snippet,authorDetails&key={API_KEY_YT}"

    if NEXT_PAGE_TOKEN:
        url += f"&pageToken={NEXT_PAGE_TOKEN}"

    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    messages = []
    try:
        items = data.get("items")
        for data_msg in items:
            user = data_msg["authorDetails"]["displayName"]
            message = data_msg["snippet"]["displayMessage"]
            messages.append((user, message))  # Retorna usuário e mensagem

        NEXT_PAGE_TOKEN = response.get("nextPageToken", None)
    except KeyError as ex:
        print(f"❌ Erro ao processar dados do YouTube: {ex}")

    return messages
