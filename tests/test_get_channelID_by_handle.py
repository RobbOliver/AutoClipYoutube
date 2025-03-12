import pytest
from unittest.mock import patch

import requests
from config import YOUTUBER_CHANNEL
from core.get_channelID_by_handle import get_channelID_by_handle
from exceptions import ChannelIDNotFoundError


# Teste simulando resposta correta


@patch('core.get_channelID_by_handle.requests.get')
def test_get_channel_id_success(mock_get):
    # Mockando o retorno da API
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "items": [{"id": "CHANNEL_ID_EXEMPLO"}]
    }

    expected_result = {
        "Handle": YOUTUBER_CHANNEL,
        "ChannelID": "CHANNEL_ID_EXEMPLO"
    }

    result = get_channelID_by_handle()

    assert result == expected_result

# Teste simulando resposta sem ID (sem canais encontrados)


@patch('core.get_channelID_by_handle.requests.get')
def test_get_channel_id_not_found(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "items": []
    }

    with pytest.raises(ChannelIDNotFoundError, match="❌ No channels found for this handle."):
        get_channelID_by_handle()


# Teste simulando erro de requisição (ex: conexão falhou)


@patch('core.get_channelID_by_handle.requests.get')
def test_get_channel_id_request_error(mock_get):
    mock_get.side_effect = requests.RequestException("Erro de conexão")

    with pytest.raises(ChannelIDNotFoundError, match="❌ HTTP request error: Erro de conexão"):
        get_channelID_by_handle()
