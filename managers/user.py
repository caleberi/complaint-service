from fastapi import HTTPException
from passlib.context import CryptContext
from asyncpg import UniqueViolationError
from db import database
from managers.auth import AuthManager
from models import users, RoleType

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserManager:
    @staticmethod
    async def register(user_data):
        user_data["password"] = pwd_context.hash(user_data.get("password"))
        try:
            id_ = await database.execute(users.insert().values(**user_data))
        except UniqueViolationError:
            raise HTTPException(400, "User with this email already exist")
        user = await database.fetch_one(users.select().where(users.c.id == id_))
        return AuthManager.encode_token(user)

    @staticmethod
    async def login(user_data):
        user = await database.fetch_one(
            users.select().where(users.c.email == user_data.get("email"))
        )
        print(f"user : {user.__str__()}")
        if not user:
            raise HTTPException(401, "Wrong password or email")
        elif not pwd_context.verify(user_data.get("password"), user["password"]):
            raise HTTPException(400, "Wrong password or email")
        return AuthManager.encode_token(user)

    @staticmethod
    async def get_all_users():
        return await database.fetch_all(users.select())

    @staticmethod
    async def get_user_by_email(email):
        return await database.fetch_all(users.select().where(users.c.email == email))

    @staticmethod
    async def change_role(role: RoleType, user_id):
        await database.execute(
            users.update().where(users.c.id == user_id).values(role=role)
        )
