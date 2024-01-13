from login_test import perform_login
from decouple import config

def test_successful_login():
    username = config('USER_ID')
    password = config('PASSWORD')
    result = perform_login(username, password)
    assert result is True

def test_failed_login():
    username = 'invalid_user'
    password = 'invalid_password'
    result = perform_login(username, password)
    assert result is False
