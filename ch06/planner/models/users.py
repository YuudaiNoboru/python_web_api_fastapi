from pydantic import BaseModel, EmailStr
from models.events import Event

class User(BaseModel):
    email: EmailStr
    password: str
    event: list[Event] | None = None

    class Config:
        schema_extra = {
            "example": {
                "email": "fastapi@packt.com.",
                "username": "strong!!!",
                "event": [],
            }
        }

class NewUser(User):
    pass

class UserSingIn(BaseModel):
    email: EmailStr
    password: str
    
    class Config:
        schema_extra = {            
                "example": {
                    "email": "fastapi@packt.com.",
                    "username": "strong!!!",
                    "event": [],
                }
            }