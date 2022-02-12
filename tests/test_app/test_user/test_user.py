from curses.ascii import US
from sqlalchemy.orm import Session

from app.user.service import create_user, PWD_CTX
from app.user.schemas import UserCreate

def test_create_user(db: Session):
    uc = UserCreate(email="test@example.com", password="test")
    user = create_user(db, uc)

    assert user.email == uc.email
    assert PWD_CTX.verify(uc.password, user.hashed_password)