from referral_system.in_memory_user_repository import (
    InMemoryUserRepository,
)
from referral_system.user import User


def test_save_and_get_user() -> None:
    """Verify that a saved user can be retrieved by user ID."""

    repository = InMemoryUserRepository()

    user = User(
        user_id=1,
        name="Jayesh",
        email="jayesh@example.com",
        contact="9726017133",
    )

    repository.save(user)
    saved_user = repository.get_by_id(1)

    assert saved_user == user


def test_get_missing_user_returns_none() -> None:
    """Verify that requesting an unknown user returns None."""

    repository = InMemoryUserRepository()

    saved_user = repository.get_by_id(99)

    assert saved_user is None


