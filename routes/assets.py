from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from controllers.assets_controller import handle_list_assets

router = APIRouter(prefix="/assets", tags=["assets"])

@router.get("/")
def list_assets(db: Session = Depends(get_db)):
    return handle_list_assets(db)
