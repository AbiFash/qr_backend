from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from controllers.scan_controller import handle_scan

router = APIRouter(prefix="/scan", tags=["scan"])

@router.get("/{code}")
def scan(code: str, db: Session = Depends(get_db)):
    return handle_scan(db, code)
