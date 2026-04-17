# Winter PEP Training - Comprehensive Python to Django Development Course

## Overview
This repository contains a comprehensive training curriculum spanning 22 days, covering foundational Python concepts through advanced Django web development. The Winter PEP (Python and Enterprise Programming) training program is designed to build practical skills in modern web development, from basic programming fundamentals to professional Django applications.

## Course Structure

### Phase 1: Python Fundamentals (Days 1-9)
Introduction to core Python concepts and programming basics.
- **Days 1-3**: Python basics, loops, data structures
- **Days 4-5**: String operations, exception handling
- **Days 6-8**: Object-oriented programming, classes, inheritance
- **Day 9**: Introduction to Django and web basics

### Phase 2: Django Development (Days 10-12)
Building web applications with Django framework.
- **Day 10**: Multiple Django apps and project structure
- **Day 11**: Django models and database operations
- **Day 12**: Advanced models and form integration

### Phase 3: Advanced Django (Days 14-22)
Professional Django development patterns and best practices.
- **Days 14-15**: Multi-app projects and template engines
- **Days 16-17**: Database operations and todo applications
- **Days 18-19**: Advanced features and REST API development
- **Days 20-21**: URL management and email systems
- **Day 22**: Complete assignment projects

## Getting Started

### Prerequisites
- Python 3.x installed
- Basic understanding of command line
- Text editor or IDE (VS Code, PyCharm, etc.)
- pip (Python package manager)

### Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd Winter_pep_training
   ```

2. For Python projects (Days 1-9):
   ```bash
   cd Day<number>
   python filename.py
   ```

3. For Django projects (Days 10+):
   ```bash
   cd Day<number>/<project_name>
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt  # If available
   python manage.py migrate
   python manage.py runserver
   ```

## Directory Structure

```
Winter_pep_training/
├── Day1/             # Python Basics
├── Day2/             # Loops and String Operations
├── Day3/             # Data Structures
├── Day4/             # String Methods
├── Day5/             # Exception Handling
├── Day6/             # Classes and OOP
├── Day7/             # Class Methods
├── Day8/             # Advanced Classes
├── Day9/             # Django Introduction
├── Day10/            # Django Multi-App Projects
├── Day11/            # Django Models and Database
├── Day12/            # Advanced Models
├── Day14/            # Django Multi-App Architecture
├── Day15/            # Template Engines (Jinja2)
├── Day16/            # Database ORM Operations
├── Day17/            # Todo Application
├── Day18/            # Advanced Todo Application
├── Day19/            # REST API Development
├── Day20/            # URL Slugs
├── Day21/            # Email Notification System
├── Day22/            # Assignment Projects
└── README.md         # This file
```

## Learning Path

### Week 1: Python Fundamentals
- Print statements and basic I/O
- Conditional statements
- Loops and iterations
- String operations and methods
- Lists, dictionaries, and data structures

### Week 2: Object-Oriented Programming
- Classes and objects
- Inheritance and polymorphism
- Encapsulation and access modifiers
- Class and static methods
- Exception handling

### Week 3: Web Development Foundations
- Django framework basics
- Model-View-Template architecture
- Database design
- URL routing

### Week 4: Advanced Django
- Multiple applications
- Serializers and APIs
- Template engines
- Email systems
- Form handling

## Technologies Used

- **Python 3.x**: Core programming language
- **Django 3.x+**: Web framework
- **SQLite3**: Database system
- **Django REST Framework**: API development
- **Jinja2**: Template engine
- **HTML5/CSS3**: Frontend markup and styling
- **Pillow**: Image processing
- **PostgreSQL** (optional): Alternative database

## Key Features of This Course

✓ Progressive complexity from basics to advanced topics
✓ Hands-on projects with real-world applications
✓ Professional code practices and standards
✓ Full-stack web development coverage
✓ REST API design and implementation
✓ Database management and optimization
✓ Email and notification systems
✓ URL optimization and SEO practices

## Project Types Included

1. **Console Applications**: Pure Python programs
2. **Web Applications**: Django-based web apps
3. **REST APIs**: Full REST API implementations
4. **Database Projects**: Complex data models
5. **Multi-App Systems**: Scalable architecture examples

## How to Use This Repository

1. **Sequential Learning**: Follow Days 1-22 in order
2. **Topic-Based Learning**: Jump to specific Day folders for targeted topics
3. **Reference**: Use README files in each Day folder for detailed information
4. **Practice**: Complete exercises and modify projects to reinforce learning

## Common Commands

### Python Projects
```bash
python filename.py          # Run Python file
python -m pdb filename.py   # Debug Python file
python -i filename.py       # Interactive mode
```

### Django Projects
```bash
python manage.py runserver          # Start dev server
python manage.py migrate            # Apply database migrations
python manage.py makemigrations     # Create migrations
python manage.py createsuperuser    # Create admin user
python manage.py shell              # Interactive shell
python manage.py collectstatic      # Collect static files
python manage.py test               # Run tests
```

## Topics Covered

### Python Programming
- Variables and data types
- Control flow (if/else, loops)
- Functions and scope
- Error handling and exceptions
- Object-oriented programming
- List comprehensions
- File I/O
- Modules and packages

### Web Development
- HTTP protocol basics
- MVC/MVT architecture
- URL routing
- Views and template rendering
- Form handling and validation
- Authentication and authorization
- Database design

### Django Framework
- Models and database
- Admin panel
- View functions
- Templates
- Static files
- Middleware
- Signals
- Class-based views

### REST APIs
- REST principles
- Serializers
- ViewSets and routers
- Authentication
- Permissions
- Pagination
- API documentation

## Learning Objectives

By completing this course, you will:
- Master Python programming fundamentals
- Build web applications with Django
- Design and implement REST APIs
- Understand database management
- Write professional, maintainable code
- Deploy and manage web applications
- Follow web development best practices

## Resources and References

Each Day folder includes:
- **README.md**: Detailed information about the Day's content
- **Source Code**: Python/Django implementation files
- **Examples**: Code examples and use cases
- **Documentation**: Comments and docstrings in code

## Best Practices Emphasized

- Clean Code principles
- DRY (Don't Repeat Yourself)
- SOLID principles
- Version control (Git)
- Testing and debugging
- Documentation
- Performance optimization
- Security considerations

## Support and Questions

For specific Day information, refer to the README file in that Day's folder. Each README contains:
- Learning objectives
- Code examples
- Setup instructions
- Common commands
- Troubleshooting tips

## Course Completion

Successfully completing this course means:
- ✓ Understanding Python fundamentals thoroughly
- ✓ Building complete Django web applications
- ✓ Designing and implementing REST APIs
- ✓ Managing databases effectively
- ✓ Following professional development practices
- ✓ Ready for junior developer roles

## Notes

- Each Day builds upon previous knowledge
- Practice is essential for mastery
- Review and reinforce concepts regularly
- Experiment beyond the provided code
- Build your own projects to solidify learning

---

**Start with Day 1 and progress sequentially for best results. Happy learning!**
