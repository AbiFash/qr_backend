from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from controllers.qr_controller import handle_list_qr

router = APIRouter(prefix="/qr", tags=["qr"])

@router.get("/")
def list_qr(db: Session = Depends(get_db)):
    return handle_list_qr(db)
