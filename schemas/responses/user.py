from models import RoleType
from schemas.base import BaseUser


class UserResponse(BaseUser):
    id: int
    phone: str
    role: RoleType
    iban: str
    first_name: str
    last_name: str
