from fastapi import APIRouter
from managers.user import UserManager
from schemas.requests.user import UserRegisterRequest, UserLoginRequest

router = APIRouter(tags=["Auth"])


@router.post("/register/", status_code=201)
async def register_user(user_data: UserRegisterRequest):
    token = await UserManager.register(user_data.dict())
    return {"token": token}


@router.post("/login/", status_code=200)
async def login_user(user_data: UserLoginRequest):
    token = await UserManager.login(user_data.dict())
    return {"token": token}
