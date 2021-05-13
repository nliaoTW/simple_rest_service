import requests


def test_get_feed():
    token = 'ca9573ebe00537727b4d9e882f9a8f27e96de949'
    url = 'http://localhost:8000/api/feed/'
    header = {
        'Authorization': 'Token ' + token
    }
    resp = requests.get(url, headers=header)
    assert resp.status_code == 200