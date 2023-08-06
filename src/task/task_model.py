from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from src.user.user_model import User


class Category(BaseModel):
    name: str
    description: str
    created_at: datetime = datetime.utcnow()


class Task(BaseModel):
    title: str
    description: str
    due_date: datetime
    created_at: datetime = datetime.utcnow()
    updated_at: datetime = datetime.utcnow()
    user: User
    category: Category
