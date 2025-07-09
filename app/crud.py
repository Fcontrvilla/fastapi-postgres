 #crear leer actualiza borrar usuarios
from .models import User
from sqlalchemy.orm import Session

def get_users(db: Session):
    return db.query(User).all()

