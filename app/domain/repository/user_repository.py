from ..user_domain import UserDomain
from abc import ABCMeta, abstractmethod


class IUserRepository(metaclass=ABCMeta):
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
