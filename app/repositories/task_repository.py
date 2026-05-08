from sqlalchemy.orm import Session
from app.models.task import Task


class TaskRepository:

    @staticmethod
    def create(db: Session, task: Task):
        db.add(task)
        db.commit()
        db.refresh(task)
        return task


    @staticmethod
    def get_by_user(db: Session, user_id: int):
        return db.query(Task).filter(Task.user_id == user_id).all()


    @staticmethod
    def get_by_id(db: Session, task_id: int, user_id: int):
        return db.query(Task).filter(
            Task.id == task_id,
            Task.user_id == user_id
        ).first()


    @staticmethod
    def save(db: Session):
        db.commit()