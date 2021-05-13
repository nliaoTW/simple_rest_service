import requests


def test_get_feed():
    token = '21728c56cfa66d7ef9990f7aa1c1b1d0d69595d9'
    url = 'http://localhost:8000/api/feed/'
    header = {
        'Authorization': 'Token ' + token
    }
    resp = requests.get(url, headers=header)
    assert resp.status_code == 200