from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from controllers.auth_controller import handle_login

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login")
def login(username: str, password: str, db: Session = Depends(get_db)):
    return handle_login(db, username, password)

