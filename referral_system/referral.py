from dataclasses import dataclass
from datetime import datetime
from enum import Enum

class ReferralStatus(Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    REWARDED = "rewarded"
    CANCELLED = "cancelled"

@dataclass
class Referral:
    referral_id: int
    referrer_id: int
    referred_user_id: int
    created_at: datetime
    status: ReferralStatus

    def __post_init__(self) -> None:
        if not isinstance(self.status,ReferralStatus):
            raise TypeError("status must be referral status")
        
        if self.referrer_id == self.referred_user_id:
            raise ValueError("A user cannot refer themselves")
