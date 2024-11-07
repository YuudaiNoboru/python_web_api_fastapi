from fastapi import APIRouter, HTTPException, status
from models.users import User, UserSingIn

user_router = APIRouter(tags=["User"])

users = {}


@user_router.post("/singup")
async def sing_nes_user(data: User) -> dict:
    if data.email in users:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with supplied username exists",
        )
    users[data.email] = data
    return {"menssage": "User sucessfully registered!"}


@user_router.post("/singin")
async def sign_user_in(user: UserSingIn) -> dict:
    if user.email not in users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User does not exist."
        )
    if users[user.email].password != user.password:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Wrong credentials passed"
        )
    return {"message": "User signed in successfully."}
