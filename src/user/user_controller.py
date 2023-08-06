from nest.core import Controller, Get, Post, Depends

from src.user.user_service import UserService
from src.user.user_model import User


@Controller(tag="user", prefix="api")
class UserController:

    service: UserService = Depends(UserService)

    @Post("/register")
    async def register(self, user: User):
        return await self.service.register(user)

    @Post("/login")
    async def login(self, user: User):
        return await self.service.login(user)
    
    @Get("/get_users")
    async def get_users(self):
        return await self.service.get_users()
                
    @Get("/get_user_by_attribute/{attribute}/{value}")
    async def get_user_by_attribute(self, attribute: str, value: str):
        return await self.service.get_user_by_attribute(attribute, value)