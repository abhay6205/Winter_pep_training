# Day 10 - Django Multiple Apps and Portfolio Management

## Overview
This project demonstrates building multiple Django applications within a single project. It includes a portfolio management application showcasing how to structure and organize multiple Django apps with proper separation of concerns.

## Project Structure

```
Day10/
├── myapp/                  # Multiple Django apps project
│   ├── portfolio/          # Portfolio app
│   │   ├── models.py       # Portfolio models
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── admin.py
│   │   ├── templates/
│   │   └── ...
│   ├── myapp/              # Project settings
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── ...
│   ├── templates/          # Project templates
│   ├── static/             # Static files
│   ├── manage.py
│   ├── python-shell-code.py # Database interaction script
│   └── db.sqlite3
│
└── newapp/                 # Alternative app setup
    ├── manage.py
    ├── new1/
    ├── new2/
    ├── newapp/
    └── db.sqlite3
```

## Key Concepts Demonstrated

- **Multiple Django Apps**: Creating and managing multiple applications in one project
- **App Organization**: Proper project structure with modular apps
- **Models**: Creating database models with various field types
- **Admin Interface**: Registering models with Django admin
- **Templates**: Rendering data with Django templates
- **Static Files**: Managing CSS, JavaScript, and image assets
- **Python Shell**: Interacting with database using Django shell

## Features

### Portfolio App (myapp)
- **Details Model**: Store portfolio/profile information
  - Name field
  - Email field (unique)
  - Phone number field
  - Address field
  - String representation for admin display

- **Database Operations**: CRUD operations on portfolio items
- **Admin Management**: Manage portfolio data through Django admin
- **Form Integration**: Forms for user input

### Data Model Example
```python
class details(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField(max_length=300)
    
    def __str__(self):
        return f"{self.name} {self.email}"
```

## Setup and Installation

1. Navigate to the myapp directory:
   ```bash
   cd Day10/myapp
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install required dependencies:
   ```bash
   pip install django
   pip install pillow  # For image handling if needed
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

## Using Python Shell Scripts

The project includes `python-shell-code.py` for direct database interaction:

```bash
python manage.py shell < python-shell-code.py
```

Or add data directly in the shell:
```bash
python manage.py shell
>>> from portfolio.models import details
>>> x = details(name="John Doe", email="john.doe@example.com", phone="1234567890", address="123 Main St")
>>> x.save()
```

## Technologies Used

- **Python 3.x**: Programming language
- **Django 3.x+**: Web framework
- **SQLite3**: Database
- **HTML/CSS**: Frontend markup and styling
- **Pillow** (optional): Image processing

## Admin Panel Features

- Register models with admin
- Display data in list view
- Search by various fields
- Filter by field values
- Edit and delete records
- Custom admin actions

## Learning Objectives

- ✓ Creating multiple Django applications
- ✓ Structuring projects with proper organization
- ✓ Defining and managing database models
- ✓ Admin panel configuration
- ✓ Using Django shell for database interaction
- ✓ Form handling and data validation
- ✓ Template rendering with model data
- ✓ Static file management

## Database Models

### Details Model
Stores portfolio or profile information with the following fields:
- **name**: CharField (max_length=100)
- **email**: EmailField (unique)
- **phone**: CharField (max_length=15)
- **address**: TextField (max_length=300)

## Common Commands

```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run shell
python manage.py shell

# Collect static files
python manage.py collectstatic
```

## Project Variations

This project includes two different application setups:

### Setup 1: myapp (Main Learning Project)
- Demonstrates portfolio management
- Includes portfolio app with proper structure
- Best for understanding app organization

### Setup 2: newapp (Alternative)
- Alternative app configuration
- Includes multiple apps (new1, new2)
- Useful for exploring different project structures

## Notes

This project is essential for understanding how to build scalable Django applications with multiple distinct apps, each handling specific functionality while maintaining clean project structure and separation of concerns.
