# Day 16 - Database Operations and ORM

## Overview
This project demonstrates database operations using Django's Object-Relational Mapping (ORM) system. It serves as a practical guide for implementing database models, migrations, and CRUD operations with Django.

## Project Structure

```
Day16/
└── dbdemo/                 # Main Django project
    ├── app/                # Application with database models
    │   ├── models.py       # Database model definitions
    │   ├── views.py
    │   ├── admin.py
    │   └── ...
    ├── dbdemo/             # Project settings
    │   ├── settings.py
    │   ├── urls.py
    │   └── ...
    ├── migrations/         # Database migrations
    ├── manage.py           # Django management script
    └── db.sqlite3          # SQLite database
```

## Key Concepts Demonstrated

- **Django ORM**: Using Models to interact with databases
- **Model Definition**: Creating database models with fields and relationships
- **Migrations**: Creating and applying database schema changes
- **CRUD Operations**: Create, Read, Update, Delete operations
- **Database Queries**: Filtering, ordering, and aggregating data
- **Admin Interface**: Using Django admin panel for database management

## Features

- **Model Definitions**: Comprehensive model examples with various field types
- **Database Migrations**: Version control for database schema
- **Query Optimization**: Efficient database querying techniques
- **Admin Configuration**: Customized Django admin panel
- **Data Relationships**: Foreign keys and relationship management

## Setup and Installation

1. Navigate to the project directory:
   ```bash
   cd Day16/dbdemo
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

7. Access the admin panel at `http://localhost:8000/admin/`

## Technologies Used

- **Python 3.x**: Programming language
- **Django**: Web framework with ORM
- **SQLite3**: Database
- **Django ORM**: Object-Relational Mapping

## Common Commands

```bash
# Create new app migrations
python manage.py makemigrations

# Apply migrations to database
python manage.py migrate

# Run database shell
python manage.py dbshell

# Create admin superuser
python manage.py createsuperuser

# Access Python shell with Django context
python manage.py shell
```

## Learning Objectives

- ✓ Understanding Django Models and fields
- ✓ Creating and managing database migrations
- ✓ Implementing CRUD operations with ORM
- ✓ Writing efficient database queries
- ✓ Configuring Django admin for models
- ✓ Managing relationships between models

## Database Schema

The project includes various model definitions showcasing:
- CharField, IntegerField, TextField, DateField
- Foreign Key relationships
- Model methods and string representations
- Meta options for model configuration

## Notes

This project provides a solid foundation for understanding Django's ORM capabilities and best practices for database design and management in web applications.
