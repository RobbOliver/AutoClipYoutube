from unittest.mock import patch

import pytest
import requests
# ajuste conforme o nome correto
from core.get_videoID import get_videoID_by_channelID
from exceptions import VideoIDNotFoundError

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


# Teste simulando resposta sem ID (sem canais encontrados)


@patch('core.get_videoID.requests.get')
def test_get_videoID_by_channelID_not_found(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "items": []
    }

    with pytest.raises(VideoIDNotFoundError, match="❌ Nenhuma live ativa encontrada para este canal."):
        get_videoID_by_channelID({"ChannelID": "EXEMPLO_CHANNEL_ID"})

# Teste simulando erro de requisição (ex: conexão falhou)


@patch('core.get_videoID.requests.get')
def test_get_videoID_by_channelID_request_error(mock_get):
    mock_get.side_effect = requests.RequestException("Erro de conexão")

    with pytest.raises(VideoIDNotFoundError, match="❌ Erro na requisição HTTP: Erro de conexão"):
        get_videoID_by_channelID({"ChannelID": "EXEMPLO_CHANNEL_ID"})

# Teste simulando erro de processamento de dados


@patch('core.get_videoID.requests.get')
def test_get_videoID_by_channelID_data_error(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {}

    with pytest.raises(VideoIDNotFoundError, match="❌ Nenhuma live ativa encontrada para este canal."):
        get_videoID_by_channelID({"ChannelID": "EXEMPLO_CHANNEL_ID"})
