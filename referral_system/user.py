from dataclasses import dataclass

@dataclass
class User:
    user_id: int
    name: str
    email: str
    contact: str
    # constructor for User class
    # def __init__(self,user_id: int,name: str,email: str,contact: str) -> None:
    #     self.user_id = user_id
    #     self.name = name
    #     self.email = email
    #     self.contact = contact
    
    # # displays the formatted User class object (encapsulation)
    # def __str__(self) -> str:
    #     return(
    #         f"User(user_id={self.user_id},name={self.name},email={self.email},contact={self.contact})"
    #     )