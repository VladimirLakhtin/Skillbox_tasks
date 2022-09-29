from main import app, client
from model import Kitties

def test_get():
    res = client.get('/kitties')

    assert res.status_code == 200
    assert len(res.get_json()) == len(Kitties.query.all())

def test_post():
    data = {
        'name': 'Test_kitty',
        'age': 12,
        'breed': 'gray',
        'description': 'My cat cat cat...',
        'image_url': 'https://www.1zoom.ru/big2/21/100325-yana.jpg'
        }

    res = client.post('/kitties', json=data)

    assert res.status_code == 200

    assert res.get_json()['name'] == data['name']

def test_put():
    res = client.put('/kitties/1', json={'name': 'Kitty_cat'})

    assert res.status_code == 200
    assert Kitties.query.get(1).name == 'Kitty_cat'

def test_delete():
    res = client.delete('/kitties/1')

    assert res.status_code == 204
    assert Kitties.query.get(1) is None

