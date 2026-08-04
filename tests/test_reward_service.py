from datetime import datetime

from referral_system.fixed_reward_policy import FixedRewardPolicy
from referral_system.in_memory_referral_repository import (
    InMemoryReferralRepository,
)
from referral_system.in_memory_reward_repository import (
    InMemoryRewardRepository,
)
from referral_system.reward_calculator import RewardCalculator
from referral_system.reward_service import RewardService
from referral_system.referral import Referral, ReferralStatus

import pytest


def test_create_duplicate_reward_raises_value_error() -> None:
    """Verify that a reward cannot be created twice for the same referral."""

    referral_repository = InMemoryReferralRepository()
    reward_repository = InMemoryRewardRepository()

    calculator = RewardCalculator(
        FixedRewardPolicy()
    )

    service = RewardService(
        reward_repository=reward_repository,
        referral_repository=referral_repository,
        reward_calculator=calculator,
    )

    referral = Referral(
        referral_id=1,
        referrer_id=1,
        referred_user_id=2,
        created_at=datetime.now(),
        status=ReferralStatus.COMPLETED,
    )

    referral_repository.save(referral)

    service.create_reward(
        reward_id=1,
        referral_id=1,
    )

    with pytest.raises(ValueError):
        service.create_reward(
            reward_id=2,
            referral_id=1,
        )


def test_create_reward_successfully() -> None:
    """Verify that a reward is created for a completed referral."""

    referral_repository = InMemoryReferralRepository()
    reward_repository = InMemoryRewardRepository()

    calculator = RewardCalculator(
        FixedRewardPolicy()
    )

    service = RewardService(
        reward_repository=reward_repository,
        referral_repository=referral_repository,
        reward_calculator=calculator,
    )

    referral = Referral(
        referral_id=1,
        referrer_id=1,
        referred_user_id=2,
        created_at=datetime.now(),
        status=ReferralStatus.COMPLETED,
    )

    referral_repository.save(referral)

    reward = service.create_reward(
        reward_id=1,
        referral_id=1,
    )

    assert reward.amount == 100