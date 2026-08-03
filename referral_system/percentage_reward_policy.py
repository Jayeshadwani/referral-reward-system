from decimal import Decimal
from referral_system.referral import Referral, ReferralStatus
from referral_system.reward_policy import RewardPolicy

class PercentageRewardPolicy(RewardPolicy):
    def __init__(self,purchase_amount: Decimal, percentage: Decimal) -> None:
        # Encapsulation - Object protects itself from being created in an invalid state
        if purchase_amount < 0:
            raise ValueError("Purchase amount cannot be negative")

        if percentage < 0 or percentage > 100:
            raise ValueError("Percentage must be between 0 and 100")

        self.purchase_amount = purchase_amount
        self.percentage = percentage
    
    def calculate_reward(self,referral: Referral) -> Decimal:
        if referral.status == ReferralStatus.COMPLETED:
            return self.purchase_amount * self.percentage / Decimal("100")
        return Decimal("0.0")