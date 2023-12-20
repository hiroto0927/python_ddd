from typing import List
from ..models.user_model import User
from sqlalchemy.orm import Session
from domain.repository.user_repository import IUserRepository
from domain.user_domain import UserDomain


class UserPersistence:
    def __init__(self, db: Session):
        self.db = db

    def find_all(self) -> list[UserDomain]:
        users = self.db.query(User).all()
        self.db.close()
        return convert_user_model_to_user_domain_list(users)

    def find_by_id(self, id: int) -> UserDomain:
        user = self.db.query(User).filter(User.id == id).first()
        if user is None:
            raise ValueError("user is not found")
        self.db.close()
        return convert_user_model_to_user_domain(user)

    def create(self, name: str, age: int) -> UserDomain:
        new_user = User(name=name, age=age)
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        self.db.close()
        return convert_user_model_to_user_domain(new_user)

    def delete(self, id: int) -> None:
        user = self.db.query(User).filter(User.id == id)
        if user is None:
            raise ValueError("user is not found")
        user.delete()
        self.db.commit()


def new_user_persistence(db: Session) -> IUserRepository:
    return UserPersistence(db)


def convert_user_model_to_user_domain(user: User) -> UserDomain:
    return UserDomain(user.name, user.age)


def convert_user_model_to_user_domain_list(users: List[User]) -> list[UserDomain]:
    return [convert_user_model_to_user_domain(user) for user in users]
