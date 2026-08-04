from sqlalchemy import select
from sqlalchemy.orm import Session

from referral_system.reward import Reward
from referral_system.reward_model import RewardModel
from referral_system.reward_repository import RewardRepository


# Class method(cls.), Instance method(self.), and Static method(no cls. nor self.)
class SQLAlchemyRewardRepository(RewardRepository):
    """Store and retrieve rewards using SQLAlchemy."""

    def __init__(self, session: Session) -> None:
        self.session = session

    def save(self, reward: Reward) -> None:
        reward_model = RewardModel(
            reward_id=reward.reward_id,
            referral_id=reward.referral_id,
            user_id=reward.user_id,
            amount=reward.amount,
        )

        self.session.add(reward_model)
        self.session.commit()

    def get_by_id(self, reward_id: int) -> Reward | None:
        statement = select(RewardModel).where(RewardModel.reward_id == reward_id)

        reward_model = self.session.scalar(statement)

        if reward_model is None:
            return None

        return self._to_domain(reward_model)

    def find_by_referral_id(
        self,
        referral_id: int,
    ) -> Reward | None:
        statement = select(RewardModel).where(RewardModel.referral_id == referral_id)

        reward_model = self.session.scalar(statement)

        if reward_model is None:
            return None

        return self._to_domain(reward_model)

    @staticmethod  # no access to self/current object
    def _to_domain(reward_model: RewardModel) -> Reward:
        """Convert a database reward model into a domain object."""

        return Reward(
            reward_id=reward_model.reward_id,
            referral_id=reward_model.referral_id,
            user_id=reward_model.user_id,
            amount=reward_model.amount,
        )
