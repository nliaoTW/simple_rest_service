import requests


def test_get_profile():
    url = 'http://localhost:8000/api/profile/'
    resp = requests.get(url)
    assert resp.status_code == 200