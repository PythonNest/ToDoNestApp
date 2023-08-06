import time

from fastapi import HTTPException

from src.user.user_model import User
from src.user.user_entity import User as UserEntity
from nest.core.decorators import db_request_handler
from functools import lru_cache


@lru_cache()
class UserService:

    @db_request_handler
    async def register(self, user: User):
        if await UserEntity.find_one({"username": user.username}):
            raise Exception("User already exists")
        new_user = UserEntity(
            **user.dict()
        )
        await new_user.save()
        time.sleep(10)
        return new_user.id

    @db_request_handler
    async def login(self, user: User):
        user_exists = await UserEntity.find_one({"username": user.username})
        if not user_exists:
            return HTTPException(status_code=404, detail="User not found")

        if user_exists.password != user.password:
            return HTTPException(status_code=401, detail="Wrong password")

        print(f"User {user.dict()} logged in")
        return user_exists.id

    @db_request_handler
    async def get_users(self):
        return await UserEntity.find_all().to_list()

    @db_request_handler
    async def get_user_by_attribute(self, attribute: str, value: str):
        att_type = User.__dict__['__fields__'][attribute].type_
        if att_type == int:
            value = int(value)
        elif att_type == float:
            value = float(value)
        elif att_type == bool:
            value = bool(value)
        elif att_type == str:
            value = str(value)
        else:
            raise HTTPException(status_code=400, detail="Attribute type not supported")
        entity_attribute = getattr(UserEntity, attribute)
        entities = await UserEntity.find_many(entity_attribute == value).to_list()
        if not entities:
            raise HTTPException(status_code=404,
                                detail="Product not found with attribute {attribute} and value {value}")
        return entities
