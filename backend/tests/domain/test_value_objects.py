import pytest
from sofilmes.domain.value_objects.email_vo import Email
from sofilmes.domain.value_objects.senha_vo import Password

def test_valid_email():
    email = Email("user@example.com")
    assert email.value() == "user@example.com"

def test_invalid_email():
    with pytest.raises(ValueError):
        Email("invalid-email")

def test_str_email():
    email = Email("user@example.com")
    assert str(email) == "user@example.com"


def test_valid_password():
    pwd = Password("Secret123")
    assert pwd.value() == "Secret123"

def test_invalid_password():
    with pytest.raises(ValueError):
        Password("short")

def test_password_hidden_str():
    pwd = Password("Secret123")
    assert str(pwd) == "*********"