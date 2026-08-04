from referral_system.reward import Reward
from referral_system.reward_repository import RewardRepository


class InMemoryRewardRepository(RewardRepository):
    def __init__(self) -> None:
        self.rewards: dict[int, Reward] = {}

    def save(self, reward: Reward) -> None:
        self.rewards[reward.reward_id] = reward

    def get_by_id(self, reward_id: int) -> Reward | None:
        return self.rewards.get(reward_id)

    def find_by_referral_id(self, referral_id: int) -> Reward | None:
        for reward in self.rewards.values():
            if reward.referral_id == referral_id:
                return reward
        
        return None