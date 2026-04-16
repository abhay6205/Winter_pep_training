# Day 14 - Django Multi-App Project

## Overview
This is a comprehensive Django project demonstrating the creation and management of multiple Django applications. The project includes separate apps for handling different functionalities: home page, about page, and service information.

## Project Structure

```
Day14/
└── main/                    # Main Django project
    ├── about/              # About app
    │   ├── views.py
    │   ├── urls.py
    │   └── ...
    ├── home/               # Home app
    │   ├── views.py
    │   ├── urls.py
    │   └── ...
    ├── main/               # Project settings
    │   ├── settings.py
    │   ├── urls.py
    │   ├── wsgi.py
    │   └── ...
    ├── service/            # Service app
    │   ├── views.py
    │   ├── urls.py
    │   └── ...
    ├── template/           # HTML templates directory
    ├── static/             # Static files (CSS, JS, images)
    ├── manage.py           # Django management script
    └── db.sqlite3          # SQLite database
```

## Key Concepts Demonstrated

- **Multiple Django Apps**: Understanding how to structure a Django project with multiple independent applications
- **URL Routing**: Implementing URL patterns across different apps
- **Templates**: Using Django templates for rendering HTML pages
- **Static Files**: Managing CSS, JavaScript, and image assets
- **Views**: Creating view functions for handling requests

## Features

- **Home App**: Landing page for the application
- **About App**: About page displaying project information
- **Service App**: Service listing and information management

## Setup and Installation

1. Navigate to the project directory:
   ```bash
   cd Day14/main
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install required dependencies:
   ```bash
   pip install django
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

6. Access the application at `http://localhost:8000/`

## Technologies Used

- **Python 3.x**: Programming language
- **Django**: Web framework
- **SQLite3**: Database
- **HTML/CSS**: Frontend markup and styling

## Learning Objectives

- ✓ Understanding Django project structure with multiple apps
- ✓ Managing URL configurations across different apps
- ✓ Creating reusable Django applications
- ✓ Template rendering and static file management
- ✓ Best practices in Django project organization

## Notes

This project serves as a foundational example for building scalable Django applications with proper separation of concerns through modular app architecture.
