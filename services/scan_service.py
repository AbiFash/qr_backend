from sqlalchemy.orm import Session
from models.qr import QRCode

def get_qr_by_code(db: Session, code: str):
    return db.query(QRCode).filter(QRCode.code == code).first()
