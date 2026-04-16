# Day 20 - URL Slugs and Article Management

## Overview
This project demonstrates URL slug implementation in Django for creating SEO-friendly URLs. It includes an article management system with slug-based URL routing, showcasing best practices for URL structure and implementation.

## Project Structure

```
Day20/
└── slug/                   # Main Django project
    ├── app/                # Application with article models
    │   ├── models.py       # Article and Student models with slugs
    │   ├── views.py
    │   ├── urls.py
    │   ├── admin.py
    │   └── ...
    ├── slug/               # Project settings
    │   ├── settings.py
    │   ├── urls.py
    │   └── ...
    ├── templates/          # HTML templates
    │   └── *.html
    ├── static/             # Static files
    ├── manage.py           # Django management script
    └── db.sqlite3          # SQLite database
```

## Key Concepts Demonstrated

- **URL Slugs**: Creating human-readable URLs
- **Slug Generation**: Automatic slug generation from text
- **Getting Objects by Slug**: Retrieving items using slugs instead of IDs
- **URL Routing**: Pattern-based URL routing with slugs
- **SEO Optimization**: Creating SEO-friendly URLs
- **Model Methods**: Using Django model methods for slug generation
- **Admin Customization**: Managing slugs in admin panel
- **Unique Constraints**: Ensuring slug uniqueness

## Features

- **Article Management**: Create, read, update, delete articles
- **Slug Generation**: Automatic slugification of article titles
- **Student Management**: Student records with slug-based URLs
- **Search by Slug**: Retrieve items using slug instead of ID
- **Admin Interface**: Manage articles and students with slug support
- **SEO-Friendly URLs**: Remove special characters and spaces from URLs
- **Unique Slugs**: Prevent duplicate slugs in database

## Setup and Installation

1. Navigate to the project directory:
   ```bash
   cd Day20/slug
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
- **Django 3.x+**: Web framework
- **SQLite3**: Database
- **django.utils.text.slugify**: Slug generation utility
- **HTML/CSS**: Frontend markup and styling

## Model Examples

### Article Model
```python
class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    slug = models.SlugField(unique=True, blank=True)
    
    def __str__(self):
        return self.title
```

### Student Model
```python
class Student(models.Model):
    name = models.CharField(max_length=100)
    reg_no = models.IntegerField(primary_key=True)
    roll_no = models.IntegerField()
    slug = models.SlugField(unique=True, blank=True)
    
    def __str__(self):
        return self.name
```

## URL Patterns

- `/article/slug-name/` - View article by slug
- `/student/name-slug/` - View student by slug
- `/articles/` - List all articles
- `/students/` - List all students

## Slug Generation Process

1. Extract title/name from the model
2. Use `slugify()` from `django.utils.text`
3. Save slug to database
4. Use slug in URL patterns for lookup

## Example Slug Transformations

| Original | Slug |
|----------|------|
| Hello World | hello-world |
| Python 3.9 | python-39 |
| Web & Mobile | web-mobile |
| Hello!!!World✓ | helloworld |

## Learning Objectives

- ✓ Understanding URL slugs and their purpose
- ✓ Implementing automatic slug generation
- ✓ Creating slug-based URL routing
- ✓ Querying objects by slug
- ✓ Ensuring slug uniqueness
- ✓ SEO optimization with clean URLs
- ✓ Admin panel customization for slugs
- ✓ Best practices for URL design

## Admin Panel Features

- Auto-generate slugs on save
- Display slugs in list view
- Search by slug
- Prevent duplicate slugs
- Edit slugs manually if needed

## Notes

This project is essential for understanding how to create SEO-friendly, human-readable URLs in Django applications and implementing professional URL structure practices.
