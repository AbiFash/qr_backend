from sqlalchemy import Column, Integer, String
from db import Base

class QRCode(Base):
    __tablename__ = "qr_codes"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(255), unique=True, index=True)
    label = Column(String(255))
    target_url = Column(String(500))
