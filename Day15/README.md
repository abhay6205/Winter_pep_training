# Day 15 - Jinja2 Template Engine with Django

## Overview
This project demonstrates the integration and usage of Jinja2 templating engine with Django. It showcases how to use Jinja2 templates alongside Django's built-in template system, exploring the differences and advantages of each approach.

## Project Structure

```
Day15/
└── jinja_project/          # Main Django project
    ├── jinja_app/          # Jinja application
    │   ├── views.py
    │   ├── urls.py
    │   └── ...
    ├── jinja_project/      # Project settings
    │   ├── settings.py
    │   ├── urls.py
    │   └── ...
    ├── templates_django/   # Django template files
    │   └── *.html
    ├── templates_jinja/    # Jinja2 template files
    │   └── *.html
    ├── manage.py           # Django management script
    └── db.sqlite3          # SQLite database
```

## Key Concepts Demonstrated

- **Jinja2 Template Engine**: Advanced templating with power template language features
- **Django Templates**: Traditional Django template syntax
- **Template Comparison**: Side-by-side comparison of Jinja2 vs Django templates
- **Configuration**: Setting up multiple template engines in Django
- **Template Inheritance**: Creating base templates and extending them
- **Control Structures**: Using loops, conditionals, and filters in templates

## Features

- **Jinja2 Templates**: Utilizing Jinja2 templating with its powerful syntax
- **Django Templates**: Standard Django template system
- **Template Switching**: Example of switching between template engines
- **Filter Demonstrations**: Using built-in and custom filters
- **Macro Usage**: Creating reusable template components with Jinja2

## Setup and Installation

1. Navigate to the project directory:
   ```bash
   cd Day15/jinja_project
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install required dependencies:
   ```bash
   pip install django jinja2
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
- **Jinja2**: Templating engine
- **SQLite3**: Database
- **HTML/CSS**: Frontend markup and styling

## Learning Objectives

- ✓ Understanding Jinja2 template syntax and features
- ✓ Comparing Jinja2 and Django template engines
- ✓ Configuring multiple template engines in Django settings
- ✓ Using filters, macros, and template inheritance
- ✓ Choosing the right templating solution for different use cases

## Template Engines Comparison

| Feature | Django Templates | Jinja2 |
|---------|-----------------|--------|
| Syntax | {% %} and {{ }} | {{ }} and {% %} |
| Filters | Limited | Extensive |
| Macros | Not available | Available |
| Performance | Good | Excellent |
| Flexibility | Good | Excellent |

## Notes

This project is ideal for learning advanced template concepts and understanding how to leverage Jinja2's powerful features within a Django application for more dynamic and flexible template management.
