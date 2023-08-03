from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.orm import Session

from db.session import get_db
from schemas.to_do import ShowTo_Do, CreateTo_Do, UpdateTo_Do
from db.repository.to_do import create_new_to_do, retrieve_to_do, list_to_dos, update_to_do, delete_to_do

from db.models.users import User
from apis.v1.route_login import get_current_user
from typing import List

router = APIRouter()

@router.post("/todo",response_model=ShowTo_Do, status_code=status.HTTP_201_CREATED)
async def create_todo(todo: CreateTo_Do, db: Session= Depends(get_db)):
    todo = create_new_to_do(todo=todo,db=db)
    return todo

@router.get("/todo/{id}", response_model=ShowTo_Do)
def get_to_do(id: int, db: Session= Depends(get_db), current_user: User=Depends(get_current_user)):
    to_do = retrieve_to_do(id=id, db=db)
    if not to_do:
        raise HTTPException(detail=f"ToDo with ID {id} does not exist.", status_code=status.HTTP_404_NOT_FOUND)
    return to_do

@router.get("/todos", response_model=List[ShowTo_Do])
def get_all_to_dos(db: Session = Depends(get_db)):
    to_dos = list_to_dos(db=db)
    return to_dos

@router.put("/todo/{id}", response_model=ShowTo_Do)
def update_to_dos(id : int, todo : UpdateTo_Do, db : Session = Depends(get_db), current_user : User=Depends(get_current_user)):
    todo = update_to_do(id=id, todo=todo, db=db)
    if isinstance(todo,dict):
        raise HTTPException(
            detail=todo.get("error"),
            status_code=status.HTTP_404_NOT_FOUND,
        )
    return todo

@router.delete("/delete/{id}")
def delete_a_to_do(id:int, db: Session = Depends(get_db), current_user: User=Depends(get_current_user)):
    message = delete_to_do(id=id, db=db)
    if message.get("error"):
        raise HTTPException(detail=message.get("error"), status_code= status.HTTP_400_BAD_REQUEST)
    return {"msg":f"Successfully deleted task with id {id}"}
