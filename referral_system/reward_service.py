from referral_system.referral import ReferralStatus
from referral_system.referral_repository import ReferralRepository
from referral_system.reward import Reward
from referral_system.reward_calculator import RewardCalculator
from referral_system.reward_repository import RewardRepository


class RewardService:
    def __init__(self, reward_repository: RewardRepository,referral_repository: ReferralRepository, reward_calculator: RewardCalculator) -> None:
        self.reward_repository = reward_repository
        self.referral_repository = referral_repository
        self.reward_calculator = reward_calculator


    def create_reward(self, reward_id: int,referral_id: int) -> Reward:
        referral = self.referral_repository.get_by_id(referral_id)

        if referral is None:
            raise ValueError("Referral does not exist")

        if referral.status != ReferralStatus.COMPLETED:
            raise ValueError("Referral must be completed before reward creation")

        existing_reward = self.reward_repository.find_by_referral_id(
            referral_id
        )

        if existing_reward is not None:
            raise ValueError("Reward already exists for this referral")

        amount = self.reward_calculator.calculate(referral)

        reward = Reward(
            reward_id=reward_id,
            referral_id=referral.referral_id,
            user_id=referral.referrer_id,
            amount=amount,
        )

        self.reward_repository.save(reward)

        return reward