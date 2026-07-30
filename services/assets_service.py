from sqlalchemy.orm import Session

def list_assets(db: Session):
    # placeholder – later map to an assets table
    return [{"id": 1, "name": "Sample asset"}]
