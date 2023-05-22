from requests import put, delete, patch, post, get
import pytest

def gen_url(config, path):
    return f'{config["main_url_api"]}{path}'

@pytest.mark.parametrize('path, code',[('users?page=2', 200), ('users/2', 200), ('users/23', 404),
                                       ('unknown', 200), ('unknown/2', 200), ('unknown/23', 404)])
def test_get_api(path, code, config):
    assert get(gen_url(config, path)).status_code == code

@pytest.mark.parametrize('path, code, params', [('users', 201, {"name": "morpheus", "job": "leader"}),
                                                ('register', 200, {"email": "eve.holt@reqres.in", "password": "pistol"}),
                                                ('register', 400, {"email": "sydney@fife"}),
                                                ('login', 200, {"email": "eve.holt@reqres.in", "password": "cityslicka"}),
                                                ('login', 400, {"email": "peter@klaven"})])
def test_post_api(path, code, params, config):
    assert post(gen_url(config, path), json=params).status_code == code

def test_put_update(config):
    params = {"name": "morpheus", "job": "zion resident"}
    assert put(gen_url(config, 'users/2'), params).ok

def test_patch_update(config):
    params = {"name": "morpheus", "job": "zion resident"}
    assert patch(gen_url(config, 'users/2'), params).ok

def test_delete_delete(config):
    assert delete(gen_url(config, 'users/2')).status_code == 204

def test_get_delayed_responce(config):
    r = get(gen_url(config, 'users?delay=3'))
    assert r.elapsed.total_seconds() > 3 and r.ok
