from decimal import Decimal

from referral_system.referral import Referral, ReferralStatus
from referral_system.reward_policy import RewardPolicy

class RewardCalculator:
    def __init__(self,policy:RewardPolicy) -> None:
        self.policy = policy
        
    def calculate(self, referral:Referral) -> Decimal:
        return self.policy.calculate_reward(referral)
        
        
    