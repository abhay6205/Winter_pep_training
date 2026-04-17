# Day 12 - Advanced Django Models and Form Integration

## Overview
This project demonstrates advanced Django model design and form integration. It builds upon basic Django concepts to showcase more sophisticated model structures, form handling, and image management in a professional Django application.

## Project Structure

```
Day12/
└── myapp/                  # Advanced Django project
    ├── portfolio/          # Portfolio application
    │   ├── models.py       # Advanced models
    │   ├── forms.py        # Django forms
    │   ├── views.py
    │   ├── urls.py
    │   ├── admin.py
    │   ├── templates/
    │   ├── python-shell-code.py  # Database operations script
    │   └── ...
    ├── myapp/              # Project settings
    │   ├── settings.py
    │   ├── urls.py
    │   └── ...
    ├── templates/          # Project-wide templates
    ├── static/             # Static files
    ├── manage.py
    └── db.sqlite3
```

## Key Concepts Demonstrated

- **Advanced Models**: Multiple models with different purposes
- **Model Fields**: Various field types including ImageField
- **Auto Timestamps**: Using auto_now for automatic timestamps
- **Form Integration**: Django forms for data validation
- **File Uploads**: Handling image uploads with ImageField
- **Admin Customization**: Advanced admin configuration
- **Model Relationships**: Managing multiple related models
- **Model Methods**: Custom methods in models

## Features

### Portfolio App
Contains two main models demonstrating different use cases:

#### Details Model
- **Name**: CharField for person's name
- **Email**: EmailField with unique constraint
- **Phone**: CharField for contact number
- **Address**: TextField for address information
- String representation for admin display

#### FormModel
- **Title**: CharField for form title
- **Description**: TextField for detailed description
- **Last Modified**: DateTimeField with auto_now (auto-updates on save)
- **Image**: ImageField for uploading images
- Automatic timestamp tracking
- Custom string representation

### Data Models Example
```python
class details(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField(max_length=300)
    
    def __str__(self):
        return f"{self.name} {self.email}"

class FormModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    last_modified = models.DateTimeField(auto_now=True)
    img = models.ImageField(upload_to='images/', blank=True, null=True)
    
    def __str__(self):
        return self.title
```

## Setup and Installation

1. Navigate to the project directory:
   ```bash
   cd Day12/myapp
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install required dependencies:
   ```bash
   pip install django
   pip install pillow  # Required for ImageField
   ```

4. Configure MEDIA settings in settings.py:
   ```python
   MEDIA_URL = '/media/'
   MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
   ```

5. Apply migrations:
   ```bash
   python manage.py migrate
   ```

6. Create migrations for new models:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

7. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

8. Start the development server:
   ```bash
   python manage.py runserver
   ```

9. Access the application at `http://localhost:8000/`

10. Access admin panel at `http://localhost:8000/admin/`

## Technologies Used

- **Python 3.x**: Programming language
- **Django 3.x+**: Web framework
- **Pillow**: Image processing library
- **SQLite3**: Database
- **HTML/CSS**: Frontend markup and styling

## Advanced Features

### ImageField Configuration
```python
# In model
img = models.ImageField(
    upload_to='images/',  # Upload directory
    blank=True,           # Optional field
    null=True             # Can be null in database
)
```

### Auto Timestamp Field
```python
# Auto-updates whenever the model instance is saved
last_modified = models.DateTimeField(auto_now=True)

# Sets timestamp only on creation
created_at = models.DateTimeField(auto_now_add=True)
```

### Django Forms Example
```python
from django import forms
from .models import FormModel

class FormModelForm(forms.ModelForm):
    class Meta:
        model = FormModel
        fields = ['title', 'description', 'img']
```

## Admin Configuration

### Registering Models
```python
from django.contrib import admin
from .models import details, FormModel

@admin.register(details)
class DetailsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone']
    search_fields = ['name', 'email']
    list_filter = ['name']

@admin.register(FormModel)
class FormModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'last_modified']
    readonly_fields = ['last_modified']
```

## Using Python Shell

```bash
# Run shell script
python manage.py shell < python-shell-code.py

# Interactive shell
python manage.py shell

# In shell:
>>> from portfolio.models import details, FormModel
>>> d = details(name="John", email="john@example.com", phone="123456", address="123 St")
>>> d.save()
>>> fm = FormModel(title="My Form", description="Form description")
>>> fm.save()
```

## Common Commands

```bash
# Create models
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Django shell
python manage.py shell

# Collect static files
python manage.py collectstatic

# Run tests
python manage.py test
```

## Learning Objectives

- ✓ Designing complex database models
- ✓ Using various Django field types
- ✓ Handling file uploads with ImageField
- ✓ Implementing automatic timestamps
- ✓ Creating and validating forms
- ✓ Customizing admin interface
- ✓ Managing media files in Django
- ✓ Model organization and structure
- ✓ Best practices in model design

## Media Files Management

### Settings Configuration
```python
# In settings.py
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

### URL Configuration
```python
# In main urls.py
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... your patterns
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

## File Upload Workflow

1. User selects image through form
2. Image uploaded to MEDIA_ROOT
3. File path stored in database
4. Display image in template using {{ object.img.url }}

## Notes

This project is crucial for understanding advanced Django model design, form handling, and media file management. It demonstrates professional practices for building feature-rich web applications with proper file handling and data validation.
