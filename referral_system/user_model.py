# from sqlalchemy import String
# from sqlalchemy.orm import Mapped, mapped_column

# from referral_system.database import Base


# class UserModel(Base):
#     """Database representation of a user."""

#     __tablename__ = "users"

#     user_id: Mapped[int] = mapped_column(primary_key=True)
#     name: Mapped[str] = mapped_column(String(100))
#     email: Mapped[str] = mapped_column(String(255), unique=True)
#     contact: Mapped[str] = mapped_column(String(20))

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from referral_system.database import Base

class UserModel(Base):
    """Database representation of a user."""

    __tablename__ = "users"

    user_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(255),unique=True)
    contact: Mapped[str] = mapped_column(String(20))

    


