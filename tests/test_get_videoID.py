from unittest.mock import patch
# ajuste conforme o nome correto
from core.get_videoID import get_videoID_by_channelID

# Teste simulando resposta correta


@patch('core.get_videoID.requests.get')
def test_get_videoID_by_channelID_success(mock_get):
    # Mock do retorno da API
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "items": [{"id": {"videoId": "VIDEO_ID_EXEMPLO"}}]
    }

    data_streamer = {"ChannelID": "EXEMPLO_CHANNEL_ID"}

    expected_result = {**data_streamer, "videoId": "VIDEO_ID_EXEMPLO"}

    result = get_videoID_by_channelID(data_streamer)

    assert result == expected_result
