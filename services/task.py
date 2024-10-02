from ..models.database import get_db
from ..repositories.task import TaskRepository
from ..schemas.task import *


class TaskService:
    def __init__(self, repository: TaskRepository):
        self.repository = repository

    def create(self, task: TaskCreateSchema) -> TaskOutSchema:
        return self.repository.create(task, next(get_db()))

    def read_all(self) -> list[TaskOutSchema]:
        return self.repository.read_all(next(get_db()))

    def read(self, task_id: int) -> TaskOutSchema:
        return self.repository.read(task_id, next(get_db()))

    def update(self, task: TaskUpdateSchema) -> TaskOutSchema:
        return self.repository.update(task, next(get_db()))

    def delete(self, task_id: int) -> TaskOutSchema:
        return self.repository.delete(task_id, next(get_db()))