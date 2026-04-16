# Day 18 - Advanced Todo Site

## Overview
This is an advanced version of a Todo management application showcasing more sophisticated Django patterns and features. It includes enhanced functionality, better architecture, and improved user experience for todo management.

## Project Structure

```
Day18/
└── todo_site/              # Main Django project
    ├── todo/               # Todo application with models and views
    │   ├── models.py
    │   ├── views.py
    │   ├── urls.py
    │   ├── forms.py
    │   ├── admin.py
    │   └── ...
    ├── todo_site/          # Project settings
    │   ├── settings.py
    │   ├── urls.py
    │   ├── wsgi.py
    │   └── ...
    ├── templates/          # HTML templates directory
    │   └── *.html
    ├── static/             # Static files (CSS, JS, images)
    ├── manage.py           # Django management script
    └── db.sqlite3          # SQLite database
```

## Key Concepts Demonstrated

- **Models**: Comprehensive Todo model with relationships
- **Views**: Class-based and function-based views
- **Forms**: Django forms with validation
- **Templates**: Template inheritance and advanced rendering
- **URL Routing**: Clean and organized URL patterns
- **Admin Customization**: Enhanced Django admin panel
- **Static Files**: Proper static file management
- **User Interface**: Professional UI/UX design

## Features

- **Todo Management**: Complete CRUD operations
- **Categories/Tags**: Organize todos by categories
- **Priority Levels**: Mark todos with priority levels
- **Due Dates**: Track deadline for todos
- **Search/Filter**: Find todos by various criteria
- **User Assignments**: Assign todos to different users (if multi-user)
- **Status Tracking**: Track todo completion status
- **Responsive Design**: Mobile-friendly interface

## Setup and Installation

1. Navigate to the project directory:
   ```bash
   cd Day18/todo_site
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

6. Collect static files (if needed):
   ```bash
   python manage.py collectstatic
   ```

7. Start the development server:
   ```bash
   python manage.py runserver
   ```

8. Access the application at `http://localhost:8000/`

9. Access admin panel at `http://localhost:8000/admin/`

## Technologies Used

- **Python 3.x**: Programming language
- **Django 3.x+**: Web framework
- **SQLite3**: Database
- **HTML5/CSS3**: Frontend markup and styling
- **JavaScript**: Interactive features
- **Bootstrap** (optional): CSS framework for styling

## Application Features

### Todo Operations
- Create new todos with title and description
- Edit existing todos
- Delete todos
- Mark todos as complete/incomplete
- Set priority levels
- Assign due dates
- Categorize todos

### User Features
- Todo listing with pagination
- Search functionality
- Filter by status/priority/date
- Recent todos view
- Sorting options

## Learning Objectives

- ✓ Building advanced Django applications
- ✓ Implementing class-based views
- ✓ Creating custom forms and validation
- ✓ Template inheritance and organization
- ✓ Advanced URL routing patterns
- ✓ Admin panel customization
- ✓ Frontend integration with backend
- ✓ User experience best practices

## Database Models

The application includes models for:
- User profiles (if multi-user)
- Todo items with all attributes
- Categories/Tags for organization
- Todo status tracking
- Activity logs (optional)

## Notes

This advanced todo application demonstrates professional Django development practices and serves as a good example for building feature-rich web applications with proper scalability and maintainability.
