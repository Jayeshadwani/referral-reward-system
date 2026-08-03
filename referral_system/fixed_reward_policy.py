from decimal import Decimal

from referral_system.referral import Referral, ReferralStatus
from referral_system.reward_policy import RewardPolicy


class FixedRewardPolicy(RewardPolicy):

    def calculate_reward(self, referral: Referral) -> Decimal:
        if referral.status == ReferralStatus.COMPLETED:
            return Decimal("100.00")

        return Decimal("0.00")