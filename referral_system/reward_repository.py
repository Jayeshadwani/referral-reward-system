from abc import ABC, abstractmethod
from referral_system.reward import Reward

class RewardRepository(ABC):

    @abstractmethod
    def save(self, reward: Reward) -> None:
        pass

    @abstractmethod
    def get_by_id(self, reward_id: int) -> Reward | None:
        pass

    @abstractmethod
    def find_by_referral_id(self, referral_id: int) -> Reward | None:
        pass