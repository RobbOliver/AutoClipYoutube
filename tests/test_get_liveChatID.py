import pytest
import requests

from exceptions import ChatIDNotFoundError
from core.get_liveChatID import get_liveChatID
from unittest.mock import patch


# Teste simulando resposta correta


@patch('core.get_liveChatID.requests.get')
def test_get_liveChatID_success(mock_get):
    mock_get.return_value.json.return_value = {
        "items": [
            {
                "liveStreamingDetails": {
                    "activeLiveChatId": "123"
                }
            }
        ]
    }

    streamer_data = {
        "videoId": "123"
    }

    result = get_liveChatID(streamer_data)
    assert result == {"videoId": "123", "liveChatId": "123"}


# Teste simulando resposta sem chat ao vivo


@patch('core.get_liveChatID.requests.get')
def test_get_liveChatID_no_chat(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "items": []
    }

    streamer_data = {
        "videoId": "123"
    }

    with pytest.raises(ChatIDNotFoundError, match='❌ Nenhum chat ao vivo encontrado para este vídeo.') as ex:
        get_liveChatID(streamer_data)


# Teste simulando erro de requisição (ex: conexão falhou)


@patch('core.get_liveChatID.requests.get')
def test_get_liveChatID_request_error(mock_get):
    mock_get.side_effect = requests.RequestException("Erro de conexão")

    streamer_data = {
        "videoId": "123"
    }

    with pytest.raises(ChatIDNotFoundError, match='❌ Erro na requisição HTTP: Erro de conexão') as ex:
        get_liveChatID(streamer_data)
