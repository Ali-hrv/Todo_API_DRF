# TODO API with Django Rest Framework

A simple TODO API project built using Django and Django Rest Framework.  
This project uses **pre-commit hooks** with **black, isort, and ruff** to ensure clean, readable, and maintainable code.

## Features

- Create, Read, Update, Delete (CRUD) for TODO items
- API structured with Django Rest Framework
- Code quality enforced with:
  - **black** (code formatting)
  - **isort** (import sorting)
  - **ruff** (linting)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/USERNAME/todo-api-drf.git
cd todo-api-drf

    Create a virtual environment:

python3 -m venv .venv
source .venv/bin/activate

    Install dependencies:

uv pip install -r requirements.txt

    Run migrations:

python manage.py migrate

    Run the development server:

python manage.py runserver

Access the API at: http://127.0.0.1:8000/
