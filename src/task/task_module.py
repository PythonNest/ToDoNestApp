from src.task.task_service import TaskService
from src.task.task_controller import TaskController


class TaskModule:

    def __init__(self):
        self.providers = [TaskService]
        self.controllers = [TaskController]



