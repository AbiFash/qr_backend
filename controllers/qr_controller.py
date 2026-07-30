from sqlalchemy.orm import Session
from services.qr_service import list_qr_codes

def handle_list_qr(db: Session):
    qrs = list_qr_codes(db)
    return [{"id": q.id, "code": q.code, "label": q.label} for q in qrs]
