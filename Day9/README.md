# Day 9 - Introduction to Django and Web Basics

## Overview
Day 9 marks the transition from pure Python to web development using Django. This day covers the basics of Django framework, its architecture, and how it facilitates building web applications using the Model-View-Template (MVT) architecture.

## Learning Objectives

- ✓ Understanding Django framework
- ✓ Learning MVC/MVT architecture
- ✓ Creating first Django project
- ✓ Understanding Django apps
- ✓ Basic URL routing
- ✓ Introduction to models and views

## Project Files

### mysite/
The Django project directory containing:
- **db.sqlite3**: SQLite database for the project
- **manage.py**: Django management script
- **mysite/**: Project settings package
  - settings.py: Project configuration
  - urls.py: URL routing
  - wsgi.py: Web server gateway interface
- **polls/**: Sample Django app
  - models.py: Database models
  - views.py: View functions
  - urls.py: App-specific URL routing
  - admin.py: Django admin configuration
  - templates/: HTML template files

## Key Concepts Covered

### 1. Django Framework
Python web framework for rapid development:
```
Django provides:
- ORM (Object-Relational Mapping)
- Admin interface
- Authentication system
- URL routing
- Template engine
- Forms handling
- Middleware support
```

### 2. MVT Architecture
Model-View-Template pattern:
```
Request Flow:
1. URL Dispatcher (urls.py)
   ↓
2. View (views.py) - processes request
   ↓
3. Model (models.py) - manages data
   ↓
4. Template (html files) - renders response
   ↓
Response
```

### 3. Models
Define database structure:
```python
from django.db import models

class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.question

class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text
```

### 4. Views
Handle business logic:
```python
from django.shortcuts import render
from .models import Poll

def index(request):
    latest_polls = Poll.objects.all()
    context = {'latest_polls': latest_polls}
    return render(request, 'polls/index.html', context)

def detail(request, poll_id):
    poll = Poll.objects.get(id=poll_id)
    return render(request, 'polls/detail.html', {'poll': poll})
```

### 5. URLs
Map URLs to views:
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:poll_id>/', views.detail, name='detail'),
]
```

### 6. Templates
Render HTML with data:
```html
<!-- polls/index.html -->
<h1>Latest Polls</h1>
<ul>
{% for poll in latest_polls %}
    <li>
        <a href="{% url 'detail' poll.id %}">
            {{ poll.question }}
        </a>
    </li>
{% endfor %}
</ul>
```

## Topics Discussed

1. **Django Basics**
   - What is Django
   - Why use Django
   - Django ecosystem
   - Prerequisites

2. **Project Structure**
   - Project vs App
   - Directory organization
   - Configuration files
   - Database setup

3. **Database Models**
   - Defining models
   - Field types
   - Relationships (ForeignKey, ManyToMany)
   - Model methods

4. **URL Routing**
   - URL patterns
   - Named URLs
   - URL parameters
   - Include function

5. **Views**
   - Function-based views
   - View parameters
   - Response objects
   - Context data

6. **Templates**
   - Template tags (if, for)
   - Template variables
   - Template filters
   - URL reverse

7. **Admin Interface**
   - Registering models
   - Customizing admin
   - Admin actions
   - Permissions

## Activities

### Activity 1: Create Django Project
```bash
# In terminal
django-admin startproject mysite
cd mysite
python manage.py startapp polls
```

### Activity 2: Define Models
In `polls/models.py`:
```python
from django.db import models

class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField()

class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```

### Activity 3: Create Views
In `polls/views.py`:
```python
from django.shortcuts import render
from .models import Poll

def index(request):
    polls = Poll.objects.all()
    return render(request, 'polls/index.html', {'polls': polls})
```

### Activity 4: Setup URLs
In `polls/urls.py`:
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

In `mysite/urls.py`:
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
]
```

### Activity 5: Create Template
In `polls/templates/polls/index.html`:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Polls</title>
</head>
<body>
    <h1>Polls</h1>
    <ul>
    {% for poll in polls %}
        <li>{{ poll.question }}</li>
    {% endfor %}
    </ul>
</body>
</html>
```

## Code Examples

### Complete Poll Model
```python
from django.db import models
from django.utils import timezone

class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.question
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - timezone.timedelta(days=1)

class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text
```

### View with Database Query
```python
from django.shortcuts import render, get_object_or_404
from .models import Poll

def index(request):
    latest_polls = Poll.objects.order_by('-pub_date')[:5]
    context = {'latest_polls': latest_polls}
    return render(request, 'polls/index.html', context)

def detail(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    context = {'poll': poll}
    return render(request, 'polls/detail.html', context)
```

### Template with Conditionals
```html
<h1>{{ poll.question }}</h1>

{% if error_message %}
    <p><strong>{{ error_message }}</strong></p>
{% endif %}

<form method="post" action="{% url 'vote' poll.id %}">
    {% csrf_token %}
    {% for choice in poll.choice_set.all %}
        <input type="radio" name="choice" value="{{ choice.id }}">
        <label>{{ choice.choice_text }}</label><br>
    {% endfor %}
    <input type="submit" value="Vote">
</form>
```

## Django Project Setup

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install Django
pip install django

# Create project
django-admin startproject myproject
cd myproject

# Create app
python manage.py startapp myapp

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run server
python manage.py runserver
```

## Common Concepts

### QuerySet Operations
```python
# Get all
Poll.objects.all()

# Filter
Poll.objects.filter(pub_date__year=2024)

# Get single
Poll.objects.get(id=1)

# Order
Poll.objects.order_by('-pub_date')

# Count
Poll.objects.count()

# Exclude
Poll.objects.exclude(votes=0)
```

### Template Tags
```html
<!-- Loop -->
{% for item in items %}
    {{ item }}
{% endfor %}

<!-- Conditional -->
{% if user.is_authenticated %}
    Welcome {{ user.name }}
{% else %}
    Please login
{% endif %}

<!-- Include -->
{% include 'header.html' %}

<!-- URL reverse -->
<a href="{% url 'detail' poll.id %}">Details</a>
```

## Common Mistakes to Avoid

1. **Forgetting INSTALLED_APPS**
   ```python
   # In settings.py
   INSTALLED_APPS = [
       'django.contrib.admin',
       'django.contrib.auth',
       'polls',  # Must add your app
   ]
   ```

2. **Not Running Migrations**
   ```bash
   # Always run after changing models
   python manage.py makemigrations
   python manage.py migrate
   ```

3. **Wrong Template Path**
   ```
   # Django looks in app_name/templates/app_name/
   # Structure must be:
   polls/
   ├── templates/
   │   └── polls/
   │       ├── index.html
   │       └── detail.html
   ```

## Practical Applications

### Web Development Patterns
- Blog with posts and comments
- E-commerce with products and orders
- Social media with users and posts
- Task management systems
- Content management systems

## Setup and Execution

1. Navigate to Day9 folder:
   ```bash
   cd Day9
   ```

2. Setup Django:
   ```bash
   cd mysite
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py runserver
   ```

3. Access application:
   - Website: http://localhost:8000/polls/
   - Admin: http://localhost:8000/admin/

## Next Steps

After Day 9, you should:
- Understand Django basics
- Understand MVT architecture
- Be able to create simple Django apps
- Be ready for Django multi-app projects (Day 10)

## Concepts to Review

- Django framework structure
- MVT architecture
- Models and databases
- URL routing
- Views and templates
- Django admin panel

## Key Takeaways

1. Django follows MVT architecture
2. Models define database structure
3. Views handle business logic
4. URLs route requests to views
5. Templates render HTML
6. Admin panel manages data
7. Django is batteries-included framework

## Additional Practice

Try these exercises:
1. Create a complete poll application
2. Add more functionality to views
3. Create custom templates
4. Use Django ORM for queries
5. Customize the admin panel
6. Create a blog application with posts

## Technologies

- **Python 3.x**: Programming language
- **Django 3.x+**: Web framework
- **SQLite3**: Default database
- **HTML/CSS**: Frontend

## Resources

- Django Official Documentation: https://docs.djangoproject.com/
- Django Girls Tutorial: https://tutorial.djangogirls.org/
- Real Python Django Tutorials: https://realpython.com/

## Notes

Day 9 is the bridge between Python fundamentals and professional web development. Django is one of the most popular web frameworks in the world. Understanding its basics opens doors to building real-world web applications.