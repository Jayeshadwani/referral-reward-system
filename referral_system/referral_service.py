from referral_system.referral import Referral
from referral_system.referral_repository import ReferralRepository
from referral_system.user_repository import UserRepository

class ReferralService:
    def __init__(self, referral_repository: ReferralRepository, user_repository: UserRepository) -> None:
        self.referral_repository = referral_repository
        self.user_repository = user_repository
    
    def create_referral(self, referral: Referral) -> None:
        referrer = self.user_repository.get_by_id(referral.referrer_id)

        referred_user = self.user_repository.get_by_id(referral.referred_user_id)

        if referrer is None:
            raise ValueError("Referrer does not exist")
        
        if referred_user is None:
            raise ValueError("Referred user does not exist")
        
        existing_referral = (
            self.referral_repository.find_by_referred_user_id(
                referral.referred_user_id
            )
        )

        if existing_referral is not None:
            raise ValueError("User has already been referred")
        
        self.referral_repository.save(referral)
    
    

    def get_referral(self, referral_id: int) -> Referral | None:
        return self.referral_repository.get_by_id(referral_id)
