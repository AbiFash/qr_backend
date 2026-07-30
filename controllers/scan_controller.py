from sqlalchemy.orm import Session
from services.scan_service import get_qr_by_code

def handle_scan(db: Session, code: str):
    qr = get_qr_by_code(db, code)
    if not qr:
        return {"found": False}
    return {"found": True, "target_url": qr.target_url}
