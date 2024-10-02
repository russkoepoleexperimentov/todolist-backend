from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from ..models.database import get_db
from ..models.task import Task
from ..schemas.task import *


class TaskRepository:
    def create(self, schema: TaskCreateSchema, db: Session) -> TaskOutSchema:
        db_task = Task(**schema.model_dump())
        db.add(db_task)
        db.commit()
        db.refresh(db_task)
        return db_task

    def read_all(self, db: Session) -> list[TaskOutSchema]:
        tasks = db.query(Task).all()
        return tasks

    def read(self, task_id: int, db: Session) -> TaskOutSchema:
        task = db.query(Task).filter(Task.id == task_id).first()
        if task is None:
            raise HTTPException(status_code=404, detail="Task not found")
        return task

    def update(self, task: TaskUpdateSchema, db: Session ) -> TaskOutSchema:
        db_task = db.query(Task).filter(Task.id == task.id).first()
        if db_task is None:
            raise HTTPException(status_code=404, detail="Task not found")

        if task.description is not None:
            db_task.description = task.description
        if task.done is not None:
            db_task.done = task.done

        db.commit()
        db.refresh(db_task)
        return db_task

    def delete(self, task_id: int, db: Session)-> TaskOutSchema:
        db_task = db.query(Task).filter(Task.id == task_id).first()
        if db_task is None:
            raise HTTPException(status_code=404, detail="Task not found")

        db.delete(db_task)
        db.commit()
        return db_task