# Day 17 - Todo Application

## Overview
This is a practical Todo management application built with Django. It demonstrates full-stack web application development including models, views, templates, and user interaction patterns for a real-world use case.

## Project Structure

```
Day17/
└── todo/                   # Main Django project
    ├── main/               # Application with todo functionality
    │   ├── models.py       # Todo model definition
    │   ├── views.py        # View functions for CRUD operations
    │   ├── urls.py         # URL routing
    │   ├── admin.py
    │   └── ...
    ├── todo/               # Project settings
    │   ├── settings.py
    │   ├── urls.py
    │   └── ...
    ├── templates/          # HTML templates
    │   └── *.html
    ├── static/             # Static files (CSS, JS)
    ├── manage.py           # Django management script
    └── db.sqlite3          # SQLite database
```

## Key Concepts Demonstrated

- **Models**: Todo model with fields for task management
- **Views**: Function-based views for CRUD operations
- **Templates**: HTML templates for rendering UI
- **URL Routing**: URL patterns for different operations
- **Forms**: Django forms for input validation
- **Admin Panel**: Managing todos through Django admin
- **Database**: Sqlite3 for data persistence

## Features

- **Create Todos**: Add new tasks with descriptions
- **Read Todos**: View list of all todos
- **Update Todos**: Edit existing todo items
- **Delete Todos**: Remove completed or unwanted todos
- **Status Tracking**: Mark todos as complete/incomplete
- **User Interface**: Clean and intuitive todo management interface

## Setup and Installation

1. Navigate to the project directory:
   ```bash
   cd Day17/todo
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install required dependencies:
   ```bash
   pip install django
   ```

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser for admin access:
   ```bash
   python manage.py createsuperuser
   ```

6. Start the development server:
   ```bash
   python manage.py runserver
   ```

7. Access the application at `http://localhost:8000/`

8. Access admin panel at `http://localhost:8000/admin/`

## Technologies Used

- **Python 3.x**: Programming language
- **Django**: Web framework
- **SQLite3**: Database
- **HTML/CSS**: Frontend markup and styling
- **JavaScript**: Interactive features (optional)

## Application Endpoints

- `/` - View all todos
- `/create/` - Create a new todo (if implemented)
- `/edit/<id>/` - Edit a specific todo
- `/delete/<id>/` - Delete a specific todo
- `/complete/<id>/` - Mark todo as complete

## Learning Objectives

- ✓ Building complete CRUD application with Django
- ✓ Implementing models with appropriate fields
- ✓ Creating views for different operations
- ✓ Designing user-friendly templates
- ✓ Handling form submissions and validations
- ✓ Managing application state and user interaction
- ✓ Best practices in web development workflow

## Todo Model Fields

- **id**: Primary key (auto-generated)
- **title**: Task title/description
- **description**: Detailed description
- **created_at**: Creation timestamp
- **completed**: Boolean flag for completion status
- **due_date**: Optional due date for the task

## Notes

This application serves as an excellent hands-on project for learning Django fundamentals and understanding how to build functional web applications with proper data management and user interface design.
