from nest.core import Controller, Get, Post, Depends

from src.task.task_service import TaskService
from src.task.task_model import Task


@Controller("task", prefix="api")
class TaskController:

    service: TaskService = Depends(TaskService)
    
    @Get("/get_tasks")
    async def get_tasks(self):
        return await self.service.get_tasks()
                
    @Post("/add_task")
    async def add_task(self, task: Task):
        return await self.service.add_task(task)

    @Get("/get_task/{id}")
    async def get_task(self, id: str):
        return await self.service.get_task(id)
 