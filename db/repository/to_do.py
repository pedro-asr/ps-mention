from sqlalchemy.orm import Session 
from schemas.to_do import CreateTo_Do, UpdateTo_Do
from db.models.to_do import To_do


def create_new_to_do(todo: CreateTo_Do, db: Session):
    to_do = To_do(**todo.dict())
    db.add(to_do)
    db.commit()
    db.refresh(to_do)
    return to_do

def retrieve_to_do(id: int, db: Session):
    to_do = db.query(To_do).filter(To_do.id == id).first()
    print("Titulo:", to_do.title)
    return to_do

def list_to_dos(db : Session):
    to_dos = db.query(To_do).all()
    return to_dos

def update_to_do(id:int, todo: UpdateTo_Do, db: Session):
    to_do_in_db = db.query(To_do).filter(To_do.id == id).first()
    if not to_do_in_db:
        return 
    to_do_in_db.title = todo.title
    to_do_in_db.description = todo.description
    db.add(to_do_in_db)
    db.commit()
    return to_do_in_db

def delete_to_do(id:int, db:Session):
    to_do_in_db = db.query(To_do).filter(To_do.id == id)
    if not to_do_in_db.first():
        return {"error":f"Could not find task with id {id}"}
    to_do_in_db.delete()
    db.commit()
    return {"msg":f"deleted task with id {id}"}