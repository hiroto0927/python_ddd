from app.domain.user_domain import UserDomain
import pytest


def test_user_domain():
    user = UserDomain("test", 20)
    assert user.name == "test"
    assert user.age == 20


def test_user_domain_name():
    with pytest.raises(TypeError):
        UserDomain(1, 20)

    with pytest.raises(ValueError):
        UserDomain("", 20)


def test_user_domain_age():
    with pytest.raises(TypeError):
        UserDomain("test", "20")

    with pytest.raises(ValueError):
        UserDomain("test", -1)


def test_user_domain_name_setter():
    user = UserDomain("test", 20)
    with pytest.raises(TypeError):
        user.name = 1

    with pytest.raises(ValueError):
        user.name = ""

    user.name = "test2"
    assert user.name == "test2"


def test_user_domain_age_setter():
    user = UserDomain("test", 20)
    with pytest.raises(TypeError):
        user.age = "20"

    with pytest.raises(ValueError):
        user.age = -1

    user.age = 21
    assert user.age == 21
