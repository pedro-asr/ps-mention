from fastapi import APIRouter

from apis.v1 import route_user, route_todo, route_login


api_router = APIRouter()
api_router.include_router(route_user.router,prefix="",tags=["users"])
api_router.include_router(route_todo.router,prefix="",tags=["todos"])
api_router.include_router(route_login.router, prefix="", tags=["login"])