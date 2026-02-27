# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build modern, high-performance REST APIs using the FastAPI framework. You'll create a fully functional API with multiple endpoints, data validation, and proper HTTP responses. This assignment will help you master asynchronous programming, request/response handling, and API design best practices.

## 📝 Tasks

### 🛠️ Create a Todo API with FastAPI

#### Description

Build a RESTful API for managing a todo list using FastAPI. Your API should allow users to create, read, update, and delete todo items. You'll implement proper request validation, error handling, and HTTP status codes to create a production-ready API.

#### Requirements

Your API must:

- Define a Todo data model with fields: `id`, `title`, `description`, `completed` (boolean)
- Implement GET endpoint to retrieve all todos
- Implement GET endpoint to retrieve a specific todo by ID
- Implement POST endpoint to create a new todo with validation
- Implement PUT endpoint to update an existing todo
- Implement DELETE endpoint to remove a todo
- Return appropriate HTTP status codes (200, 201, 404, 400)
- Include input validation using Pydantic models
- Handle errors gracefully with meaningful error messages

### 🛠️ Test Your API

#### Description

Create comprehensive tests to verify that your API endpoints work correctly and handle edge cases properly. Use the provided test file to ensure all functionality is working as expected.

#### Requirements

Your tests should:

- Test successful creation and retrieval of todos
- Test updating todo items with valid and invalid data
- Test deletion of todos
- Test error cases (e.g., invalid IDs, missing required fields)
- Verify correct HTTP status codes are returned
- Ensure data validation works properly
