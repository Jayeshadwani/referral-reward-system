from sqlalchemy import select
from sqlalchemy.orm import Session

from referral_system.referral import Referral
from referral_system.referral_model import ReferralModel
from referral_system.referral_repository import ReferralRepository


class SQLAlchemyReferralRepository(ReferralRepository):
    """Store and retrieve referrals using SQLAlchemy."""

    def __init__(self, session: Session) -> None:
        self.session = session

    def save(self, referral: Referral) -> None:
        referral_model = ReferralModel(
            referral_id=referral.referral_id,
            referrer_id=referral.referrer_id,
            referred_user_id=referral.referred_user_id,
            created_at=referral.created_at,
            status=referral.status,
        )

        # update an existing record if exists else create using merge
        self.session.merge(referral_model)
        self.session.commit()

    def get_by_id(self, referral_id: int) -> Referral | None:
        # Builds the SQL query
        statement = select(ReferralModel).where(
            ReferralModel.referral_id == referral_id
        )

        # executes the query and returns single record
        referral_model = self.session.scalar(statement)

        if referral_model is None:
            return None

        return Referral(
            referral_id=referral_model.referral_id,
            referrer_id=referral_model.referrer_id,
            referred_user_id=referral_model.referred_user_id,
            created_at=referral_model.created_at,
            status=referral_model.status,
        )

    def find_by_referred_user_id(self, referred_user_id: int) -> Referral | None:
        statement = select(ReferralModel).where(
            ReferralModel.referred_user_id == referred_user_id
        )

        referral_model = self.session.scalar(statement)

        if referral_model is None:
            return None

        return Referral(
            referral_id=referral_model.referral_id,
            referrer_id=referral_model.referrer_id,
            referred_user_id=referral_model.referred_user_id,
            created_at=referral_model.created_at,
            status=referral_model.status,
        )
