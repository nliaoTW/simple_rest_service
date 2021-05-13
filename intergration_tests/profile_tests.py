import requests


def test_get_profile():
    token = 'ca9573ebe00537727b4d9e882f9a8f27e96de949'
    url = 'http://localhost:8000/api/profile/'
    header = {
        'Authorization': 'Token ' + token
    }
    resp = requests.get(url, headers=header)
    assert resp.status_code == 200
    resp_body = resp.json()
    assert resp_body[0]['email'] == 'admin@test.com'
    assert resp_body[0]['name'] == 'Nelson'