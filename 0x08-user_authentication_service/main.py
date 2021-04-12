#!/usr/bin/env python3
"""
Module for main.py
0x08. User authentication service
Holberton Web Stack programming Spec ― Back-end
"""
import requests

BASEURL = 'http://127.0.0.1:5000'


def register_user(email: str, password: str) -> None:
    """
    POST /users route
    """
    data = {
        'email': email,
        'password': password
    }
    response = requests.post(f"{BASEURL}/users", data=data)
    assert response.status_code == 200
    assert response.json() == {'email': email, 'message': 'user created'}


def log_in_wrong_password(email: str, password: str) -> None:
    """
    POST /sessions route
    """
    data = {
        'email': email,
        'password': password
    }
    response = requests.post(f"{BASEURL}/sessions", data=data)
    assert response.status_code == 401


def log_in(email: str, password: str) -> str:
    """
    POST /sessions route
    """
    data = {
        'email': email,
        'password': password
    }
    response = requests.post(f"{BASEURL}/sessions", data=data)
    assert response.status_code == 200
    assert response.json() == {'email': email, 'message': 'logged in'}
    return response.cookies.get('session_id')


def profile_unlogged() -> None:
    """
    GET /profile route
    """
    cookies = {'session_id': None}
    response = requests.get(f"{BASEURL}/profile", cookies=cookies)
    assert response.status_code == 403


def profile_logged(session_id: str) -> None:
    """
    GET /profile route
    """
    cookies = {'session_id': session_id}
    response = requests.get(f"{BASEURL}/profile", cookies=cookies)
    assert response.status_code == 200
    assert response.json() == {'email': EMAIL}


def log_out(session_id: str) -> None:
    """
    DELETE /sessions route
    """
    cookies = {'session_id': session_id}
    response = requests.delete(f"{BASEURL}/sessions", cookies=cookies)
    assert response.status_code == 200
    assert response.json() == {'message': 'Bienvenue'}


def reset_password_token(email: str) -> str:
    """
    POST /reset_password route
    """
    data = {'email': email}
    response = requests.post(f"{BASEURL}/reset_password", data=data)
    assert response.status_code == 200
    payload = response.json()
    reset_token = payload.get('reset_token')
    assert payload == {'email': email, 'reset_token': reset_token}
    return reset_token


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """
    PUT /reset_password route
    """
    data = {
        'email': email,
        'reset_token': reset_token,
        'new_password': new_password
    }
    response = requests.put(f"{BASEURL}/reset_password", data=data)
    assert response.json() == {'email': email, 'message': 'Password updated'}
    assert response.status_code == 200


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
