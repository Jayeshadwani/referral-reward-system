from referral_system.referral import Referral
from referral_system.referral_repository import ReferralRepository

class InMemoryReferralRepository(ReferralRepository):
    def __init__(self) -> None:
        self.referrals: dict[int, Referral] = {}
    
    def save(self, referral: Referral) -> None:
        self.referrals[referral.referral_id] = referral
    
    def get_by_id(self, referral_id: int) -> Referral | None:
        return self.referrals.get(referral_id)

    def find_by_referred_user_id(self, referred_user_id: int) -> Referral | None:
        for referral in self.referrals.values():
            if referral.referred_user_id == referred_user_id:
                return referral
        return None