from datetime import datetime

from referral_system.database import Base, SessionLocal, engine
from referral_system.referral import Referral, ReferralStatus
from referral_system.referral_model import ReferralModel
from referral_system.referral_service import ReferralService
from referral_system.sqlalchemy_referral_repository import (
    SQLAlchemyReferralRepository,
)
from referral_system.sqlalchemy_user_repository import (
    SQLAlchemyUserRepository,
)
from referral_system.user import User
from referral_system.user_model import UserModel
from referral_system.user_service import UserService
from referral_system.reward_model import RewardModel
from referral_system.fixed_reward_policy import FixedRewardPolicy
from referral_system.reward_calculator import RewardCalculator
from referral_system.reward_service import RewardService
from referral_system.sqlalchemy_reward_repository import (
    SQLAlchemyRewardRepository,
)


def create_database_tables() -> None:
    """Create database tables that do not already exist."""

    Base.metadata.create_all(engine)


def run_referral_flow() -> None:
    """Register users, create a referral, complete it, and create its reward."""

    with SessionLocal() as session:
        user_repository = SQLAlchemyUserRepository(session)
        referral_repository = SQLAlchemyReferralRepository(session)
        reward_repository = SQLAlchemyRewardRepository(session)

        user_service = UserService(user_repository)

        referral_service = ReferralService(
            referral_repository=referral_repository,
            user_repository=user_repository,
        )

        reward_service = RewardService(
            reward_repository=reward_repository,
            referral_repository=referral_repository,
            reward_calculator=RewardCalculator(FixedRewardPolicy()),
        )

        create_users_if_missing(user_service)

        referral = create_referral_if_missing(referral_service)

        if referral.status == ReferralStatus.PENDING:
            referral = referral_service.complete_referral(referral.referral_id)

        existing_reward = reward_repository.find_by_referral_id(referral.referral_id)

        if existing_reward is None:
            reward = reward_service.create_reward(
                reward_id=1,
                referral_id=referral.referral_id,
            )
        else:
            reward = existing_reward

        print(referral)
        print(reward)


def create_users_if_missing(user_service: UserService) -> None:
    """Create the demo users when they do not already exist."""

    users = [
        User(
            user_id=1,
            name="Jayesh",
            email="jayesh@example.com",
            contact="9726017133",
        ),
        User(
            user_id=2,
            name="Amit",
            email="amit@example.com",
            contact="9876543210",
        ),
    ]

    for user in users:
        existing_user = user_service.get_user(user.user_id)

        if existing_user is None:
            user_service.register_user(user)


def create_referral_if_missing(
    referral_service: ReferralService,
) -> Referral:
    """Create the demo referral when it does not already exist."""

    existing_referral = referral_service.get_referral(1)

    if existing_referral is not None:
        return existing_referral

    referral = Referral(
        referral_id=1,
        referrer_id=1,
        referred_user_id=2,
        created_at=datetime.now(),
        status=ReferralStatus.PENDING,
    )

    referral_service.create_referral(referral)

    return referral


def main() -> None:
    """Run the referral reward application."""

    create_database_tables()
    run_referral_flow()


if __name__ == "__main__":
    main()
