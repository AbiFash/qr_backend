from sqlalchemy.orm import Session
from models.user import User

def authenticate(db: Session, username: str, password: str):
    # placeholder – add real hashing later
    return db.query(User).filter(User.username == username).first()
