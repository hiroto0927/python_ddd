from domain.user_domain import UserDomain
from abc import ABCMeta, abstractmethod
from domain.repository.user_repository import IUserRepository


class IUserUsecase(metaclass=ABCMeta):
    @abstractmethod
    def find_all(self) -> list[UserDomain]:
        pass

    @abstractmethod
    def find_by_id(self, id: int) -> UserDomain:
        pass

    @abstractmethod
    def create(self, user: UserDomain) -> UserDomain:
        pass

    @abstractmethod
    def delete(self, id: int) -> None:
        pass


class UserUsecase(IUserUsecase):
    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository

    def find_all(self) -> list[UserDomain]:
        return self.user_repository.find_all()

    def find_by_id(self, id: int) -> UserDomain:
        return self.user_repository.find_by_id(id)

    def create(self, user: UserDomain) -> UserDomain:
        return self.user_repository.create(user)

    def delete(self, id: int) -> None:
        self.user_repository.delete(id)


def new_user_usecase(user_repository: IUserRepository) -> IUserUsecase:
    return UserUsecase(user_repository)
