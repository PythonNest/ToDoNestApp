from nest.core.database.base_odm import OdmService
from src.examples.examples_entity import Examples
import os
from dotenv import load_dotenv
from src.task.task_entity import Task
from src.user.user_entity import User

load_dotenv()
    

config = OdmService(
    db_type="mongodb",
    config_params={
        "db_name": os.getenv("DB_NAME"),
        "host": os.getenv("DB_HOST"),
        "port": os.getenv("DB_PORT"),
    },
    document_models=[User, Task, Examples]
)       
        