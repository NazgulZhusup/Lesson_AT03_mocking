import pytest
from main_cat import get_random_cat_image

def test_get_random_cat_image_success(mocker):
    mock_get = mocker.patch('main1.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [{'url': 'https://example.com/cat.jpg'}]

    image_url = get_random_cat_image()
    assert image_url == 'https://example.com/cat.jpg'

def test_get_random_cat_image_failure(mocker):
    mock_get = mocker.patch('main1.requests.get')
    mock_get.return_value.status_code = 404

    image_url = get_random_cat_image()
    assert image_url is None

if __name__ == '__main__':
    pytest.main()
