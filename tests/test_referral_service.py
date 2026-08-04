from datetime import datetime

from referral_system.in_memory_referral_repository import (
    InMemoryReferralRepository,
)
from referral_system.in_memory_user_repository import (
    InMemoryUserRepository,
)
from referral_system.referral import Referral, ReferralStatus
from referral_system.referral_service import ReferralService
from referral_system.user import User

import pytest
from datetime import datetime

def test_complete_referral_successfully() -> None:
    """Verify that a pending referral can be completed."""

    user_repository = InMemoryUserRepository()
    referral_repository = InMemoryReferralRepository()

    service = ReferralService(
        referral_repository=referral_repository,
        user_repository=user_repository,
    )

    referrer = User(
        user_id=1,
        name="Jayesh",
        email="jayesh@example.com",
        contact="9726017133",
    )

    referred = User(
        user_id=2,
        name="Rahul",
        email="rahul@example.com",
        contact="9876543210",
    )

    user_repository.save(referrer)
    user_repository.save(referred)

    referral = Referral(
        referral_id=1,
        referrer_id=1,
        referred_user_id=2,
        created_at=datetime.now(),
        status=ReferralStatus.PENDING,
    )

    service.create_referral(referral)

    completed_referral = service.complete_referral(1)

    assert completed_referral.status == ReferralStatus.COMPLETED


def test_create_duplicate_referral_raises_value_error() -> None:
    """Verify that a user cannot be referred more than once."""

    user_repository = InMemoryUserRepository()
    referral_repository = InMemoryReferralRepository()

    service = ReferralService(
        referral_repository=referral_repository,
        user_repository=user_repository,
    )

    referrer_1 = User(
        user_id=1,
        name="Jayesh",
        email="jayesh@example.com",
        contact="9726017133",
    )

    referrer_2 = User(
        user_id=2,
        name="Rahul",
        email="rahul@example.com",
        contact="9876543210",
    )

    referred_user = User(
        user_id=3,
        name="Amit",
        email="amit@example.com",
        contact="9999999999",
    )

    user_repository.save(referrer_1)
    user_repository.save(referrer_2)
    user_repository.save(referred_user)

    referral_1 = Referral(
        referral_id=1,
        referrer_id=1,
        referred_user_id=3,
        created_at=datetime.now(),
        status=ReferralStatus.PENDING,
    )

    referral_2 = Referral(
        referral_id=2,
        referrer_id=2,
        referred_user_id=3,
        created_at=datetime.now(),
        status=ReferralStatus.PENDING,
    )

    service.create_referral(referral_1)

    with pytest.raises(ValueError):
        service.create_referral(referral_2)


def test_create_referral_successfully() -> None:
    """Verify that a valid referral can be created."""

    user_repository = InMemoryUserRepository()
    referral_repository = InMemoryReferralRepository()

    service = ReferralService(
        referral_repository=referral_repository,
        user_repository=user_repository,
    )

    referrer = User(
        user_id=1,
        name="Jayesh",
        email="jayesh@example.com",
        contact="9726017133",
    )

    referred = User(
        user_id=2,
        name="Rahul",
        email="rahul@example.com",
        contact="9876543210",
    )

    user_repository.save(referrer)
    user_repository.save(referred)

    referral = Referral(
        referral_id=1,
        referrer_id=1,
        referred_user_id=2,
        created_at=datetime.now(),
        status=ReferralStatus.PENDING,
    )

    service.create_referral(referral)

    assert service.get_referral(1) == referral