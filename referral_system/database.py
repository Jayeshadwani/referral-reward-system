from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

# This tells SQLAlchemy to use SQLite and create a file named: referral_system.db
DATABASE_URL = "sqlite:///referral_system.db"


# Every SQLAlchemy ORM model will inherit from this base class. SQLAlchemy uses that inheritance to collect table definitions.
class Base(DeclarativeBase):
    """Base class for all SQLAlchemy database models."""


# Python application → Engine → SQLite database
engine = create_engine(DATABASE_URL, echo=True)

#  A session is the object through which we add, query, update, and commit database records. SQLAlchemy’s ORM transaction handling is performed through the Session.
SessionLocal = sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)
