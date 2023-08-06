from fastapi import HTTPException

from src.task.task_model import Task
from src.task.task_entity import Task as TaskEntity
from nest.core.decorators import db_request_handler
from functools import lru_cache


@lru_cache()
class TaskService:

    @db_request_handler
    async def add_task(self, task: Task):
        new_task = TaskEntity(
            **task.dict()
        )
        await new_task.save()
        return new_task.id

    @db_request_handler
    async def get_tasks(self):
        return await TaskEntity.find_all().to_list()

    @db_request_handler
    async def get_task(self, id: str):
        task = await TaskEntity.find_one(TaskEntity.id == id)
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
        return task
