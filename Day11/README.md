# Day 11 - Django Models and Database Operations

## Overview
Day 11 deepens understanding of Django's database layer through models. This day focuses on creating sophisticated models, understanding model relationships, migrations, and performing various database operations using Django's ORM.

## Project Structure

```
Day11/
└── myapp/                  # Django project
    ├── portfolio/          # Application with database models
    │   ├── models.py       # Model definitions
    │   ├── views.py
    │   ├── urls.py
    │   ├── admin.py        # Admin registration
    │   ├── migrations/
    │   └── ...
    ├── myapp/              # Project settings
    │   ├── settings.py
    │   ├── urls.py
    │   └── ...
    ├── templates/
    ├── manage.py
    ├── python-shell-code.py # ORM examples
    └── db.sqlite3
```

## Key Concepts Demonstrated

- **Model Definition**: Creating comprehensive database models
- **Field Types**: Various field types for different data
- **Model Relationships**: ForeignKey, OneToOneField, ManyToMany
- **Model Methods**: Adding functionality to models
- **QuerySet API**: Performing complex database queries
- **Migrations**: Managing database schema changes
- **Admin Configuration**: Registering and customizing models
- **Model Validation**: Field validation and constraints

## Learning Objectives

- ✓ Understanding Django Model architecture
- ✓ Creating complex database models
- ✓ Understanding model relationships
- ✓ Using Django ORM effectively
- ✓ Managing migrations
- ✓ Configuring Django admin
- ✓ Writing model methods and properties
- ✓ Performing database queries

## Model Fields Available

### Basic Fields
```python
# Text fields
name = models.CharField(max_length=100)          # Short text
bio = models.TextField()                         # Long text
slug = models.SlugField()                        # URL-safe text

# Numeric fields
age = models.IntegerField()                      # Integer
price = models.DecimalField(max_digits=10, decimal_places=2)
rating = models.FloatField()

# Boolean and nullables
is_active = models.BooleanField(default=True)
middle_name = models.CharField(max_length=100, blank=True, null=True)

# Date/Time fields
created_at = models.DateTimeField(auto_now_add=True)
updated_at = models.DateTimeField(auto_now=True)
birthday = models.DateField()

# Relationships
user = models.ForeignKey(User, on_delete=models.CASCADE)
favorite = models.OneToOneField(Article, on_delete=models.CASCADE)
tags = models.ManyToManyField(Tag)

# Other fields
email = models.EmailField()
url = models.URLField()
image = models.ImageField(upload_to='images/')
file = models.FileField(upload_to='files/')
```

## Features Covered

### 1. Model Definition
```python
from django.db import models
from django.utils import timezone

class Portfolio(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Portfolios"
    
    def __str__(self):
        return f"{self.name} - {self.email}"
```

### 2. Model Relationships
```python
class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

class Review(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE)
    content = models.TextField()

class Category(models.Model):
    name = models.CharField(max_length=100)

class Article(models.Model):
    title = models.CharField(max_length=200)
    categories = models.ManyToManyField(Category)
```

### 3. QuerySet Examples
```python
def portfolio_queries():
    # Get all
    all_items = Portfolio.objects.all()
    
    # Filter
    recent = Portfolio.objects.filter(created_at__gte=timezone.now() - timedelta(days=7))
    
    # Get single
    item = Portfolio.objects.get(id=1)
    
    # Filter with multiple conditions
    results = Portfolio.objects.filter(name__icontains='John', email__endswith='.com')
    
    # Ordering
    sorted_items = Portfolio.objects.all().order_by('-created_at')
    
    # Count
    total = Portfolio.objects.count()
    
    # Exclude
    active = Portfolio.objects.exclude(is_active=False)
    
    # Exists
    has_items = Portfolio.objects.filter(name='John').exists()
```

### 4. Migration Management
```bash
# Create migrations after model changes
python manage.py makemigrations

# View migrations
python manage.py showmigrations

# Apply migrations
python manage.py migrate

# Revert migration
python manage.py migrate app_name 0001

# Create empty migration
python manage.py makemigrations --empty app_name --name custom_name
```

### 5. Admin Configuration
```python
from django.contrib import admin
from .models import Portfolio

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created_at']
    list_filter = ['created_at', 'is_active']
    search_fields = ['name', 'email']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Personal Info', {
            'fields': ('name', 'email')
        }),
        ('Contact', {
            'fields': ('phone', 'address')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
```

### 6. Complex Queries
```python
from django.db.models import Q, Count, Avg

# OR queries
Portfolio.objects.filter(Q(name='John') | Q(name='Jane'))

# AND queries
Portfolio.objects.filter(Q(name='John') & Q(is_active=True))

# Count related items
authors = Author.objects.annotate(book_count=Count('book'))

# Average rating
articles = Article.objects.annotate(avg_rating=Avg('review__rating'))

# Aggregate
from django.db.models import Sum, Avg
stats = Order.objects.aggregate(
    total_orders=Count('id'),
    avg_price=Avg('price'),
    total_revenue=Sum('price')
)
```

## Common Model Patterns

### Timestamps
```python
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True  # Use as parent class
```

### Soft Deletes
```python
class SoftDeleteModel(models.Model):
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    def delete(self):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()
```

### Slug Fields
```python
from django.utils.text import slugify

class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
```

## Accessing Models via Django Shell

```bash
# Start Django shell
python manage.py shell

# In shell
from portfolio.models import Portfolio

# Create
p = Portfolio(name="John", email="john@example.com")
p.save()

# Read
item = Portfolio.objects.get(id=1)
items = Portfolio.objects.all()

# Update
item.name = "Jane"
item.save()

# Delete
item.delete()
```

## Field Options

```python
models.CharField(
    max_length=100,              # Maximum length
    null=True,                   # Allow NULL in database
    blank=True,                  # Allow blank in forms
    default='',                  # Default value
    unique=True,                 # Must be unique
    db_index=True,              # Create database index
    choices=[('A', 'Option A')], # Limited selections
    help_text='Help text',      # Form help text
    verbose_name='Display Name'  # Human-readable name
)
```

## Setup and Installation

1. Navigate to Day11/myapp:
   ```bash
   cd Day11/myapp
   ```

2. Create and activate environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. Install Django:
   ```bash
   pip install django
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Create superuser:
   ```bash
   python manage.py createsuperuser
   ```

6. Start server:
   ```bash
   python manage.py runserver
   ```

## Common Django Commands

```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Check migration status
python manage.py showmigrations

# Shell
python manage.py shell

# Create superuser
python manage.py createsuperuser

# Collect static
python manage.py collectstatic

# Run tests
python manage.py test

# Check system
python manage.py check
```

## File Structure

```python
# models.py - Define database structure
# views.py - Business logic and request handling
# urls.py - URL routing
# admin.py - Django admin configuration
# forms.py - Form definitions (not in basic apps)
# tests.py - Unit tests
# migrations/ - Database schema versions
# templates/ - HTML templates
# static/ - CSS, JavaScript, images
```

## Next Steps

After Day 11, you should:
- Understand Django models thoroughly
- Create complex database models
- Perform sophisticated queries
- Manage migrations effectively
- Configure admin panel
- Be ready for advanced Django (Day 12+)

## Learning Outcomes

- ✓ Design effective database schemas
- ✓ Understand ORM advantages and usage
- ✓ Perform complex database operations
- ✓ Manage schema evolution
- ✓ Use admin panel effectively
- ✓ Write testable models

## Technologies Used

- **Python 3.x**: Programming language
- **Django 3.x+**: Web framework
- **SQLite3**: Database (default)
- **PostgreSQL** (optional): Production database

## Resources

- Django Models Documentation: https://docs.djangoproject.com/en/stable/topics/db/models/
- Django QuerySet API: https://docs.djangoproject.com/en/stable/ref/models/querysets/
- Django Admin: https://docs.djangoproject.com/en/stable/ref/contrib/admin/

## Notes

Models are the foundation of any Django application. Understanding them well is crucial for professional development. Practice creating models, writing queries, and managing migrations to become proficient in Django development.