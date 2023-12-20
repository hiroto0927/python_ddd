from app.infrastructure.persistence.user_persistence import UserPersistence, new_user_persistence
from unittest.mock import MagicMock
from app.infrastructure.models.user_model import User


def test_user_persistence():
    user_persistence = UserPersistence(MagicMock())
    assert user_persistence.db is not None


def test_user_persistence_find_all():
    user_persistence = UserPersistence(MagicMock())
    user_persistence.db.query.return_value.all.return_value = [User(name="user1", age=20), User(name="user2", age=30)]
    users = user_persistence.find_all()
    assert len(users) == 2
    assert users[0].name == "user1"
    assert users[0].age == 20
    assert users[1].name == "user2"
    assert users[1].age == 30


def test_user_persistence_find_by_id():
    user_persistence = UserPersistence(MagicMock())
    user_persistence.db.query.return_value.filter.return_value.first.return_value = User(name="user1", age=20)
    user = user_persistence.find_by_id(1)
    assert user.name == "user1"
    assert user.age == 20


def test_user_persistence_find_by_id_not_found():
    user_persistence = UserPersistence(MagicMock())
    user_persistence.db.query.return_value.filter.return_value.first.return_value = None
    try:
        user_persistence.find_by_id(1)
        assert False
    except ValueError:
        assert True


def test_user_persistence_create():
    user_persistence = UserPersistence(MagicMock())
    user_persistence.create("user1", 20)
    user_persistence.db.add.assert_called_once()
    user_persistence.db.commit.assert_called_once()

    assert user_persistence.db.add.call_args[0][0].name == "user1"
    assert user_persistence.db.add.call_args[0][0].age == 20


def test_user_persistence_delete():
    user_persistence = UserPersistence(MagicMock())
    user_persistence.db.query.return_value.filter.return_value.delete.return_value = None
    user_persistence.db.commit.return_value = None
    user_persistence.delete(1)
    user_persistence.db.query.assert_called_once()
    user_persistence.db.query.return_value.filter.assert_called_once()
    user_persistence.db.query.return_value.filter.return_value.delete.assert_called_once()
    user_persistence.db.commit.assert_called_once()


def test_new_user_persistence():
    user_repository = new_user_persistence(MagicMock())
    assert user_repository is not None
