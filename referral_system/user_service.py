
from referral_system.user import User
from referral_system.user_repository import UserRepository

# main.py -> service_layer -> repository_layer -> DB layer

class UserService:
    def __init__(self,repository: UserRepository) -> None:
        self.repository = repository
    
    def register_user(self, user:User) -> None:
        existing_user = self.repository.get_by_email(user.email)

        if existing_user is not None:
            raise ValueError("Email is already registered")
        
        self.repository.save(user)
    
    def get_user(self,user_id:int) -> User | None:
        return self.repository.get_by_id(user_id)