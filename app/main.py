import uuid

from fastapi import APIRouter, FastAPI
from fastapi_users import FastAPIUsers

from app.user.models import User, UserCreate, UserRead
from app.user.utils import auth_backend, get_user_manager

app = FastAPI()

routers: list[APIRouter] = []
fastapi_users = FastAPIUsers[User, uuid.UUID](
    get_user_manager,
    [auth_backend],
)
for router in routers:
    app.include_router(router)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
