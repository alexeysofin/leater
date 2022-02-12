from curses.ascii import US
from datetime import datetime
from sqlalchemy.orm import Session

from passlib.context import CryptContext

from app.user.models import User
from app.user.schemas import UserCreate

PWD_CTX = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_user(db: Session, uc: UserCreate) -> User:
    db_user = User(
        email=uc.email,
        hashed_password=PWD_CTX.hash(uc.password),
        updated_at=datetime.utcnow(),
    )
    db.add(db_user)
    db.commit()
    return db_user
