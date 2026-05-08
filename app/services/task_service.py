from sqlalchemy.orm import Session
from app.models.task import Task
from app.repositories.task_repository import TaskRepository


class TaskService:

    @staticmethod
    def create_task(db: Session, title: str, description: str, user_id: int):
        task = Task(title=title, description=description, user_id=user_id)
        return TaskRepository.create(db, task)


    @staticmethod
    def get_user_tasks(db: Session, user_id: int):
        return TaskRepository.get_by_user(db, user_id)


    @staticmethod
    def get_task_by_id(db: Session, task_id: int, user_id: int):
        return TaskRepository.get_by_id(db, task_id, user_id)


    @staticmethod
    def update_task(task, db: Session, data: dict):
        for key, value in data.items():
            setattr(task, key, value)

        TaskRepository.save(db)
        db.refresh(task)
        return task