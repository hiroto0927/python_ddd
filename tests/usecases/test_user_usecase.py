from app.usecases.user_usecase import UserUsecase, new_user_usecase
from unittest.mock import MagicMock
from app.domain.user_domain import UserDomain


def test_user_usecase():
    user_usecase = UserUsecase(MagicMock())
    assert user_usecase.user_repository is not None


def test_user_usecase_find_all():
    user_usecase = UserUsecase(MagicMock())
    user_usecase.user_repository.find_all.return_value = [UserDomain("user1", 20), UserDomain("user2", 30)]
    users = user_usecase.find_all()
    assert len(users) == 2
    assert users[0].name == "user1"
    assert users[0].age == 20
    assert users[1].name == "user2"
    assert users[1].age == 30


def test_user_usecase_find_by_id():
    user_usecase = UserUsecase(MagicMock())
    user_usecase.user_repository.find_by_id.return_value = UserDomain("user1", 20)
    user = user_usecase.find_by_id(1)
    assert user.name == "user1"
    assert user.age == 20


def test_user_usecase_create():
    user_usecase = UserUsecase(MagicMock())
    user_usecase.user_repository.create.return_value = UserDomain("user1", 20)
    user = user_usecase.create(UserDomain("user1", 20))
    assert user.name == "user1"
    assert user.age == 20


def test_user_usecase_delete():
    user_usecase = UserUsecase(MagicMock())
    user_usecase.delete(1)
    user_usecase.user_repository.delete.assert_called_once()
    user_usecase.user_repository.delete.assert_called_once_with(1)


def test_new_user_usecase():
    user_usecase = new_user_usecase(MagicMock())
    assert user_usecase.user_repository is not None
