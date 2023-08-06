from orm_config import config
from nest.core.app import App
from src.examples.examples_module import ExamplesModule
from src.task.task_module import TaskModule
from src.user.user_module import UserModule

app = App(
    description="PyNest service",
    modules=[
        ExamplesModule,
        TaskModule,
        UserModule,
    ]
)


@app.on_event("startup")
async def startup():
    await config.create_all() 
