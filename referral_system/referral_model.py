from datetime import datetime

from sqlalchemy import DateTime, Enum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from referral_system.database import Base
from referral_system.referral import ReferralStatus


class ReferralModel(Base):
    """Database representation of a referral."""

    __tablename__ = "referrals"

    referral_id: Mapped[int] = mapped_column(primary_key=True)

    referrer_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"))

    referred_user_id: Mapped[int] = mapped_column(
        ForeignKey("users.user_id"),
        unique=True,  # one more check to verify one user is referred only once
    )

    created_at: Mapped[datetime] = mapped_column(DateTime)

    status: Mapped[ReferralStatus] = mapped_column(Enum(ReferralStatus))
