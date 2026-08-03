from referral_system.user import User
from referral_system.user_repository import UserRepository

class InMemoryUserRepository(UserRepository):
    def __init__(self) -> None:
        self.users: dict[int,User] = {}
    
    def save(self, user:User) -> None:
        self.users[user.user_id] = user
    
    def get_by_id(self, user_id:int) -> User | None:
        return self.users.get(user_id)

    def get_by_email(self, email:str) -> User | None:
        for user in self.users.values():
            if user.email == email:
                return user
        return None

    