from decimal import Decimal

from sqlalchemy import ForeignKey, Numeric
from sqlalchemy.orm import Mapped, mapped_column

from referral_system.database import Base


class RewardModel(Base):
    """Database representation of a reward."""

    __tablename__ = "rewards"

    reward_id: Mapped[int] = mapped_column(primary_key=True)

    referral_id: Mapped[int] = mapped_column(
        ForeignKey("referrals.referral_id"),
        unique=True,
    )

    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"))

    amount: Mapped[Decimal] = mapped_column(Numeric(10, 2))
