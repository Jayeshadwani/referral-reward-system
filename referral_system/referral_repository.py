from abc import ABC, abstractmethod

from referral_system.referral import Referral

class ReferralRepository(ABC):

    @abstractmethod
    def save(self, referral:Referral) -> None:
        pass

    @abstractmethod
    def get_by_id(self, referral_id: int) -> Referral | None:
        pass

    @abstractmethod
    def find_by_referred_user_id(self, referred_user_id: int) -> Referral | None:
        pass

    
