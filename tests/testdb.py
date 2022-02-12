from sqlalchemy import orm

from app.core.db import SessionLocal

Session = orm.scoped_session(SessionLocal, scopefunc=lambda: "static")