from pydantic import BaseModel,EmailStr, Field


class UserCreate(BaseModel):
    email : EmailStr
    password : str = Field(..., min_length=4)
    
class ShowUser(BaseModel):
    id: int
    email : EmailStr

    class Config():
        orm_mode = True