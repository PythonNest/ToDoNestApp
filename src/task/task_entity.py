from beanie import Document, Indexed, Link
import pymongo
from datetime import datetime
from src.user.user_entity import User


class Category(Document):
    name: str = Indexed(str, pymongo.TEXT)
    description: str
    created_at: datetime = datetime.utcnow()

    class Config:
        schema_extra = {
            "example": {
                "name": "Food",
                "description": "Food category",
                "created_at": "2021-01-01T00:00:00.000Z"
            }
        }


class Task(Document):
    title: str
    description: str
    due_date: datetime
    created_at: datetime = datetime.utcnow()
    updated_at: datetime = datetime.utcnow()
    user: Link[User]
    category: Link[Category]

    class Config:
        schema_extra = {
            "example": {
                "title": "Buy groceries",
                "description": "Buy groceries for the week",
                "due_date": "2021-01-01T00:00:00.000Z",
                "created_at": "2021-01-01T00:00:00.000Z",
                "updated_at": "2021-01-01T00:00:00.000Z",
                "user": {
                    "username": "johndoe",
                    "email": "johndoe@gmail.com",
                    "password": "123456",
                    "created_at": "2021-01-01T00:00:00.000Z"
                },
                "category": {
                    "name": "Food",
                    "description": "Food category",
                    "created_at": "2021-01-01T00:00:00.000Z"
                }
            }
        }
