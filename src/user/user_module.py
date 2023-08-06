from src.user.user_service import UserService
from src.user.user_controller import UserController


class UserModule:

    def __init__(self):
        self.providers = [UserService]
        self.controllers = [UserController]



