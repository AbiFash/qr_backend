from sqlalchemy.orm import Session
from services.assets_service import list_assets

def handle_list_assets(db: Session):
    return list_assets(db)
