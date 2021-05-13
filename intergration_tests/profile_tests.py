import requests


def test_get_profile():
    token = '21728c56cfa66d7ef9990f7aa1c1b1d0d69595d9'
    url = 'http://localhost:8000/api/profile/'
    header = {
        'Authorization': 'Token ' + token
    }
    resp = requests.get(url, headers=header)
    assert resp.status_code == 200
    resp_body = resp.json()
    assert resp_body[0]['email'] == 'admin@test.com'
    assert resp_body[0]['name'] == 'Nelson'