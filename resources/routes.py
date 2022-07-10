from fastapi import APIRouter
from .auth import router as auth_router
from .complaint import router as complaint_router
from .user import router as user_router

api_router = APIRouter()

api_router.include_router(auth_router)
api_router.include_router(complaint_router)
api_router.include_router(user_router)
