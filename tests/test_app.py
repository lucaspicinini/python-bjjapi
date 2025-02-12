from app import create_app

def test_config():
    assert not create_app('dev').testing
    assert not create_app('prod').testing
    assert create_app('test').testing