from fastapi import APIRouter, HTTPException, status
from database.connection import Database
from models.users import User, UserSingIn

user_router = APIRouter(tags=["User"])

user_database = Database(User)

@user_router.post("/singup")
async def sing_nes_user(user: User) -> dict:
    user_exist = await User.find_one(User.email == user.email)
    if user_exist:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User with supplied username exists")
    await user_database.save(user)
    return {"menssage": "User sucessfully registered!"}

@user_router.post("/singin")
async def sign_user_in(user: UserSingIn) -> dict:
    user_exist = await User.find_one(User.email == user.email)
    if not user_exist:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User does not exist.")
    if user_exist.password == user.password:
        return {"message": "User signed in successfully."}
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Wrong credentials passed")