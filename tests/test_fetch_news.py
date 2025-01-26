import pytest
from unittest.mock import Mock, patch
from plugins.operators.fetch_news import FetchNewsOperator

@patch("requests.get")
def test_fetch_news_success(mock_get):
    mock_response = Mock()
    mock_response.json.return_value = {"articles": [{"title": "Test"}]}
    mock_get.return_value = mock_response

    operator = FetchNewsOperator(
        api_url="dummy_url",
        output_path="test.parquet"
    )
    operator.execute(context=None)
    
    assert True  # Verificación básica de ejecución