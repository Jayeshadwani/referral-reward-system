from abc import ABC, abstractmethod
from decimal import Decimal

from referral_system.referral import Referral

class RewardPolicy(ABC):

    @abstractmethod
    def calculate_reward(self,reward:Referral) -> Decimal:
        pass