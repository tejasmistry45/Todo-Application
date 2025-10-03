from datetime import datetime
from uuid import uuid4

# In-memory storage (list of dictionaries)
todos = []


def create_todo(todo_data: dict) -> dict:
    """Create a new todo"""
    todo = {
        "id": str(uuid4()),
        "title": todo_data["title"],
        "description": todo_data.get("description"),
        "priority": todo_data["priority"],
        "completed": False,
        "tags": todo_data.get("tags", []),
        "created_at": datetime.now(),
        "updated_at": datetime.now()
    }
    todos.append(todo)
    return todo


def get_all_todos() -> list:
    """Get all todos"""
    return todos


def get_todo_by_id(todo_id: str) -> dict:
    """Get todo by ID"""
    for todo in todos:
        if todo["id"] == todo_id:
            return todo
    return None


def update_todo(todo_id: str, update_data: dict) -> dict:
    """Update todo"""
    todo = get_todo_by_id(todo_id)
    if not todo:
        return None
    
    for key, value in update_data.items():
        if value is not None:
            todo[key] = value
    
    todo["updated_at"] = datetime.now()
    return todo


def delete_todo(todo_id: str) -> bool:
    """Delete todo"""
    todo = get_todo_by_id(todo_id)
    if not todo:
        return False
    todos.remove(todo)
    return True


def get_stats() -> dict:
    """Get todo statistics"""
    total = len(todos)
    completed = sum(1 for todo in todos if todo["completed"])
    pending = total - completed
    high_priority = sum(1 for todo in todos if todo["priority"] == "high")
    medium_priority = sum(1 for todo in todos if todo["priority"] == "medium")
    low_priority = sum(1 for todo in todos if todo["priority"] == "low")
    
    return {
        "total": total,
        "completed": completed,
        "pending": pending,
        "high_priority": high_priority,
        "medium_priority": medium_priority,
        "low_priority": low_priority
    }
