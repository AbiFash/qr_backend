from sqlalchemy.orm import Session
from services.auth_service import authenticate

def handle_login(db: Session, username: str, password: str):
    user = authenticate(db, username, password)
    if not user:
        return {"success": False, "message": "Invalid credentials"}
    return {"success": True, "username": user.username}
