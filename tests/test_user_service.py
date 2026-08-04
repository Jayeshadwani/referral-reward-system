from referral_system.in_memory_user_repository import (
    InMemoryUserRepository,
)
from referral_system.user import User
from referral_system.user_service import UserService

import pytest



def test_register_duplicate_email_raises_value_error() -> None:
    """Verify that duplicate email registration raises a ValueError."""

    repository = InMemoryUserRepository()
    service = UserService(repository)

    user_1 = User(
        user_id=1,
        name="Jayesh",
        email="jayesh@example.com",
        contact="9726017133",
    )

    user_2 = User(
        user_id=2,
        name="Rahul",
        email="jayesh@example.com",
        contact="9876543210",
    )

    service.register_user(user_1)

    with pytest.raises(ValueError):
        service.register_user(user_2)


def test_register_user_successfully() -> None:
    """Verify that a new user can be registered successfully."""

    repository = InMemoryUserRepository()
    service = UserService(repository)

    user = User(
        user_id=1,
        name="Jayesh",
        email="jayesh@example.com",
        contact="9726017133",
    )

    service.register_user(user)

    assert service.get_user(1) == user