from typing import Generator, NoReturn

import pytest

from sqlalchemy.orm import Session
import sqlalchemy_utils as sa_utils

from app.core.db import Base, SessionLocal, engine
from app.settings import DB_URL
from app.db_tables import User # noqa

from tests import testdb

@pytest.fixture(scope="session", autouse=True)
def create_db() -> Generator[SessionLocal, None, None]:
    if sa_utils.database_exists(str(DB_URL)):
        sa_utils.drop_database(str(DB_URL))

    sa_utils.create_database(str(DB_URL))
    Base.metadata.create_all(engine)
    yield
    sa_utils.drop_database(str(DB_URL))


@pytest.fixture(scope="function")
def db(create_db: NoReturn) -> Generator[Session, None, None]:
    """
    Creates a new database session with (with working transaction)
    for test duration.
    """
    session_ = testdb.Session()
    session_.begin_nested()
    yield session_
    session_.rollback()