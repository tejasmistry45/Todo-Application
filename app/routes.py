from fastapi import APIRouter, HTTPException, status
from typing import List

from app.models import TodoCreate, TodoUpdate, TodoResponse
from app import storage

router = APIRouter(prefix="/todos", tags=["todos"])


@router.post("/", response_model=TodoResponse, status_code=status.HTTP_201_CREATED)
def create_todo(todo: TodoCreate):
    """Create a new todo"""
    new_todo = storage.create_todo(todo.dict())
    return new_todo


@router.get("/", response_model=List[TodoResponse])
def get_all_todos():
    """Get all todos"""
    return storage.get_all_todos()


@router.get("/{todo_id}", response_model=TodoResponse)
def get_todo(todo_id: str):
    """Get todo by ID"""
    todo = storage.get_todo_by_id(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


@router.put("/{todo_id}", response_model=TodoResponse)
def update_todo(todo_id: str, todo_update: TodoUpdate):
    """Update todo"""
    update_data = {k: v for k, v in todo_update.dict().items() if v is not None}
    
    if not update_data:
        raise HTTPException(status_code=400, detail="No fields to update")
    
    updated_todo = storage.update_todo(todo_id, update_data)
    if not updated_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    return updated_todo


@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id: str):
    """Delete todo"""
    success = storage.delete_todo(todo_id)
    if not success:
        raise HTTPException(status_code=404, detail="Todo not found")


@router.get("/stats/summary")
def get_todo_stats():
    """Get todo statistics"""
    return storage.get_stats()
