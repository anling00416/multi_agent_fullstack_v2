
import requests
def test_add():
    r=requests.post("http://127.0.0.1:8000/todos?title=test")
    assert r.status_code==200
