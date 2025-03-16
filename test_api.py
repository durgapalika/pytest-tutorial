from api import get_posts
import pytest

mock_return_value = {
    "userId": 1,
    "id": 1,
    "title": "some title",
    "body": "some body"
}


def test_get_posts(mocker):
    mock_get = mocker.patch("api.requests.get")

    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = mock_return_value

    result = get_posts(1)

    assert result == mock_return_value
    mock_get.assert_called_once_with("http://jsonplaceholder.typicode.com/posts/1")
