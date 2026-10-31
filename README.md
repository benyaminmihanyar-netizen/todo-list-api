# To-Do List API

A simple REST API for managing tasks with priorities, built with Python and Flask.

## Features
- Add a new task with a priority
- List all tasks
- Toggle a task's completion status
- Delete a task
- Task logic is separated from the routes using OOP (Task and TaskManager classes)

## Tech
- Python
- Flask
- requests (for testing)

## Endpoints
| Method | Route | Description |
|--------|-------|-------------|
| POST | /tasks | Create a new task |
| GET | /tasks | Get all tasks |
| PUT | /tasks/<task_id> | Update/toggle a task |
| DELETE | /tasks/<task_id> | Delete a task |

## How to Run
1. Install dependencies:
   pip install -r requirements.txt
2. Start the server:
   python app.py
3. In another terminal, run the tests:
   python test.py

## What I Learned
- Designing an API (requirements, entities, routes) before writing code
- Structuring Flask apps with OOP and separate logic functions
- Testing endpoints with the requests library