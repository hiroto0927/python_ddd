from ..db.db import Base
from sqlalchemy import Column, Integer, String
from .common_model import TimestampMixin
from domain.user_domain import UserDomain


class User(Base, TimestampMixin):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)

    def convert_to_user_domain(self) -> UserDomain:
        return UserDomain(self.name, self.age)
