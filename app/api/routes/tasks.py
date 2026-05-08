from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Optional
from sqlalchemy import or_
from app.core.database import get_db
from app.schemas.task import TaskCreate, TaskUpdate, TaskOut
from app.core.deps import get_current_user
from app.services.task_service import TaskService
from app.models.task import Task

router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.post("/")
def create_task(task: TaskCreate,
                db: Session = Depends(get_db),
                user_id: int = Depends(get_current_user)):

    return TaskService.create_task(
        db, task.title, task.description, user_id
    )


@router.get("/", response_model=list[TaskOut])
def get_tasks(
    skip: int = 0,
    limit: int = 10,
    completed: Optional[bool] = None,
    search: Optional[str] = None,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user)
):

    query = db.query(Task).filter(
        Task.user_id == user_id
    )

    # FILTER
    if completed is not None:
        query = query.filter(
            Task.completed == completed
        )

    # SEARCH
    if search:
        query = query.filter(
            or_(
                Task.title.ilike(f"%{search}%"),
                Task.description.ilike(f"%{search}%")
            )
        )

    # PAGINATION
    tasks = query.offset(skip).limit(limit).all()

    return tasks


@router.patch("/{task_id}")
def update_task(task_id: int,
                task_update: TaskUpdate,
                db: Session = Depends(get_db),
                user_id: int = Depends(get_current_user)):

    task = TaskService.get_task_by_id(db, task_id, user_id)

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    return TaskService.update_task(task, db, task_update.dict(exclude_unset=True))

@router.delete("/{task_id}")
def delete_task(
    task_id: int,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user)
):

    task = db.query(Task).filter(
        Task.id == task_id,
        Task.user_id == user_id
    ).first()

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    db.delete(task)
    db.commit()

    return {"message": "Task deleted successfully"}    