from pydantic import BaseModel


class CreateTo_Do(BaseModel):
    title: str 
    description: str
    status: bool
    
        
class ShowTo_Do(BaseModel):
    title: str 
    description: str
    status: bool

    class Config():
        orm_mode = True


class UpdateTo_Do(CreateTo_Do):
    pass
