from beanie import Document, Indexed
from datetime import datetime
import pymongo


class User(Document):
    username: Indexed(str, pymongo.TEXT)
    email: str
    password: str
    created_at: datetime = datetime.utcnow()

    class Config:
        schema_extra = {
            "example": {
                "username": "johndoe",
                "email": "johndoe@gmail.com",
                "password": "123456",
                "created_at": "2021-01-01T00:00:00.000Z"
            }
        }
