from dataclasses import dataclass
from decimal import Decimal

@dataclass
class Reward:
    reward_id: int
    referral_id: int
    user_id: int
    amount: Decimal

    def __post_init__(self) -> None:
        if self.amount <= 0:
            raise ValueError("Reward must me greater than zero")
            
