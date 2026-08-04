from sqlalchemy import select
from sqlalchemy.orm import Session

from referral_system.user import User
from referral_system.user_model import UserModel
from referral_system.user_repository import UserRepository


class SQLAlchemyUserRepository(UserRepository):
    """Store and retrieve users using SQLAlchemy."""

    def __init__(self, session: Session) -> None:
        self.session = session

    def save(self, user: User) -> None:
        user_model = UserModel(
            user_id=user.user_id, name=user.name, email=user.email, contact=user.contact
        )

        self.session.add(user_model)
        self.session.commit()

    def get_by_id(self, user_id: int) -> User | None:
        statement = select(UserModel).where(UserModel.user_id == user_id)

        user_model = self.session.scalar(statement)

        if user_model is None:
            return None

        return User(
            user_id=user_model.user_id,
            name=user_model.name,
            email=user_model.email,
            contact=user_model.contact,
        )

    def get_by_email(self, email: str) -> User | None:
        statement = select(UserModel).where(UserModel.email == email)

        user_model = self.session.scalar(statement)

        if user_model is None:
            return None

        return User(
            user_id=user_model.user_id,
            name=user_model.name,
            email=user_model.email,
            contact=user_model.contact,
        )
