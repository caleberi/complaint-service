from schemas.base import BaseUser


class UserRegisterRequest(BaseUser):
    password: str
    phone: str
    last_name: str
    first_name: str
    iban: str


class UserLoginRequest(BaseUser):
    password: str
