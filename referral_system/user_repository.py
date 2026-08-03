from abc import ABC, abstractmethod

from referral_system.user import User

# contract for user_repo that tells what things to do, not exactly how

class UserRepository(ABC):

    @abstractmethod
    def save(self,user:User) -> None:
        pass

    @abstractmethod
    def get_by_id(self, user_id:int) -> User | None:
        pass

    @abstractmethod
    def get_by_email(self, email: str) -> User | None:
        pass

    