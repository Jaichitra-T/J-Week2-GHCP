"""
FastAPI Todo API Starter Code

This is a starter template for building a RESTful API using FastAPI.
Complete the implementation to create a fully functional todo management API.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List

# Initialize FastAPI application
app = FastAPI(
    title="Todo API",
    description="A simple API for managing todo items",
    version="1.0.0"
)

# Define the Todo data model
class Todo(BaseModel):
    """Todo item data model"""
    id: Optional[int] = None
    title: str
    description: Optional[str] = None
    completed: bool = False


# In-memory storage for todos (replace with a database in production)
todos_db: List[Todo] = []
next_id = 1


# TODO: Implement GET endpoint to retrieve all todos
# GET /todos
@app.get("/todos")
async def get_all_todos():
    """Retrieve all todos"""
    # TODO: Return the list of todos
    pass


# TODO: Implement GET endpoint to retrieve a specific todo by ID
# GET /todos/{todo_id}
@app.get("/todos/{todo_id}")
async def get_todo(todo_id: int):
    """Retrieve a specific todo by ID"""
    # TODO: Find and return the todo with the given ID
    # TODO: Raise HTTPException with 404 status if todo not found
    pass


# TODO: Implement POST endpoint to create a new todo
# POST /todos
@app.post("/todos", status_code=201)
async def create_todo(todo: Todo):
    """Create a new todo"""
    # TODO: Assign an ID to the new todo
    # TODO: Add it to the todos_db list
    # TODO: Return the created todo
    pass


# TODO: Implement PUT endpoint to update a todo
# PUT /todos/{todo_id}
@app.put("/todos/{todo_id}")
async def update_todo(todo_id: int, todo_update: Todo):
    """Update an existing todo"""
    # TODO: Find the todo with the given ID
    # TODO: Update its fields
    # TODO: Return the updated todo
    # TODO: Raise HTTPException with 404 status if todo not found
    pass


# TODO: Implement DELETE endpoint to remove a todo
# DELETE /todos/{todo_id}
@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int):
    """Delete a todo"""
    # TODO: Find and remove the todo with the given ID
    # TODO: Return a success message
    # TODO: Raise HTTPException with 404 status if todo not found
    pass


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
