from referral_system.user import User
from referral_system.referral import Referral, ReferralStatus
from referral_system.fixed_reward_policy import FixedRewardPolicy
from referral_system.percentage_reward_policy import PercentageRewardPolicy
from referral_system.reward import Reward
from datetime import datetime
from decimal import Decimal
from referral_system.reward_calculator import RewardCalculator
from referral_system.in_memory_user_repository import InMemoryUserRepository
from referral_system.in_memory_referral_repository import InMemoryReferralRepository
from referral_system.user_service import UserService
from referral_system.referral_service import ReferralService

user_repository = InMemoryUserRepository()
referral_repository = InMemoryReferralRepository()

user_service = UserService(user_repository)
referral_service = ReferralService(
    referral_repository=referral_repository,
    user_repository=user_repository
)

# referrer = User(
#     user_id=1,
#     name="Jayesh",
#     email="jayesh@example.com",
#     contact="9726017133",
# )

# referred_user = User(
#     user_id=2,
#     name="Amit",
#     email="amit@example.com",
#     contact="9876543210",
# )

referrer = User(
    user_id=1,
    name="Jayesh",
    email="jayesh@example.com",
    contact="9726017133"
)

referred_user = User(
    user_id=2,
    name="Amit",
    email="amit@example.com",
    contact="9876543210"
)

user_service.register_user(referrer)
user_service.register_user(referred_user)

# referral = Referral(
#     referral_id=1,
#     referrer_id=1,
#     referred_user_id=2,
#     created_at=datetime.now(),
#     status=ReferralStatus.PENDING,
# )

referral = Referral(
    referral_id=1,
    referrer_id=1,
    referred_user_id=2,
    created_at=datetime.now(),
    status=ReferralStatus.PENDING
)

referral_service.create_referral(referral)

saved_referral = referral_service.get_referral(1)
print(saved_referral)

# user = User(user_id=1,name="Jayesh Adwani",email="jayeshadwani25@gmail.com",contact="9726017133")
# referral = Referral(referral_id=1,referrer_id=2,referred_user_id=3,created_at=datetime.now(),status=ReferralStatus.PENDING)
# reward = Reward(reward_id=1,referral_id=1,user_id=1,amount=Decimal("100.00"))

# print(user.name,user.email,user.contact)

# print(user)
# print(referral)
# print(reward)


# referral = Referral(
#     referral_id=1,
#     referrer_id=1,
#     referred_user_id=2,
#     created_at=datetime.now(),
#     status=ReferralStatus.COMPLETED,
# )

# fixed_policy = FixedRewardPolicy()
# percentage_policy = PercentageRewardPolicy(purchase_amount=Decimal("1000.00"),percentage=Decimal("5"))

# # Dependency Injection  + Polymorphism
# fixed_calculator = RewardCalculator(fixed_policy)
# reward_amount = fixed_calculator.calculate(referral)

# print(f"Fixed policy reward amount: {reward_amount}")



# percentage_calculator = RewardCalculator(percentage_policy)

# pct_reward_amount = percentage_calculator.calculate(referral)

# print(f"Percentage policy reward amount: {pct_reward_amount}")




