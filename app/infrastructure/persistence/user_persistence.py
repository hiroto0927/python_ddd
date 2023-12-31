from ..models.user_model import User
from domain.repository.user_repository import IUserRepository
from domain.user_domain import UserDomain
from ..db.db import SessionLocal


class UserPersistence:
    def __init__(self):
        self.db = SessionLocal()

    def find_all(self) -> list[UserDomain]:
        users = self.db.query(User).all()
        self.db.close()
        return list(map(lambda user: user.convert_to_user_domain(), users))

    def find_by_id(self, id: int) -> UserDomain:
        user = self.db.query(User).filter(User.id == id).first()
        if user is None:
            raise ValueError("user is not found")
        self.db.close()
        return user.convert_to_user_domain()

    def create(self, name: str, age: int) -> UserDomain:
        new_user = User(name=name, age=age)
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        self.db.close()
        return new_user.convert_to_user_domain()

    def delete(self, id: int) -> None:
        user = self.db.query(User).filter(User.id == id)
        if user is None:
            raise ValueError("user is not found")
        user.delete()
        self.db.commit()


def new_user_persistence() -> IUserRepository:
    return UserPersistence()
