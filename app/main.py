# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/")
# def root():
#     return {"message": "Hello World"}

from domain.user_domain import UserDomain

user = UserDomain("John", 20)
print(user.name)
print(user.age)

user.name = "aa"

print(user.name)
