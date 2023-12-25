from app.infrastructure.persistence.user_persistence import UserPersistence, new_user_persistence
from unittest.mock import MagicMock
from app.infrastructure.models.user_model import User


def test_user_persistence_find_all():
    user_persistence = UserPersistence()
    user_persistence.db = MagicMock()
    user_persistence.db.query.return_value.all.return_value = [
        User(name="test1", age=20),
        User(name="test2", age=21),
    ]

    users = user_persistence.find_all()

    assert len(users) == 2
    assert users[0].name == "test1"
    assert users[0].age == 20
    assert users[1].name == "test2"
    assert users[1].age == 21


def test_user_persistence_find_by_id():
    user_persistence = UserPersistence()
    user_persistence.db = MagicMock()
    user_persistence.db.query.return_value.filter.return_value.first.return_value = User(name="test1", age=20)

    user = user_persistence.find_by_id(1)

    assert user.name == "test1"
    assert user.age == 20


def test_user_persistence_create():
    user_persistence = UserPersistence()
    user_persistence.db = MagicMock()
    user_persistence.db.add.return_value = None
    user_persistence.db.commit.return_value = None
    user_persistence.db.refresh.return_value = None
    user_persistence.db.close.return_value = None

    user = user_persistence.create("test1", 20)

    assert user.name == "test1"
    assert user.age == 20


def test_user_persistence_delete():
    user_persistence = UserPersistence()
    user_persistence.db = MagicMock()
    user_persistence.db.query.return_value.filter.return_value.delete.return_value = None
    user_persistence.db.commit.return_value = None

    user_persistence.delete(1)


def test_new_user_persistence():
    user_persistence = new_user_persistence()

    assert isinstance(user_persistence, UserPersistence)
