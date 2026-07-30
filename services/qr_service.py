from sqlalchemy.orm import Session
from models.qr import QRCode

def list_qr_codes(db: Session):
    return db.query(QRCode).limit(50).all()
