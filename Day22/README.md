# Day 22 - Assignment Projects

## Overview
This directory contains a series of assignment projects showcasing progressive complexity in Django development. Each assignment builds upon previous concepts and introduces new features and best practices.

## Project Structure

```
Day22/
├── ass1/                   # Assignment 1 - Basic Django App
│   ├── db.sqlite3
│   ├── manage.py
│   ├── app/
│   ├── ass1/
│   └── screenshots/
│
├── assignment2/            # Assignment 2 - REST API Implementation
│   ├── db.sqlite3
│   ├── manage.py
│   ├── test_api.py        # API testing script
│   ├── app/               # App with serializers
│   ├── assignment2/
│   └── screenshots/
│
├── assignment3/            # Assignment 3 - Advanced Features
│   ├── db.sqlite3
│   ├── manage.py
│   ├── test_api.py
│   ├── app/
│   ├── assignment3/
│   └── screenshots/
│
└── assignment4/            # Assignment 4 - Complex Implementation
    ├── db.sqlite3
    ├── manage.py
    ├── test_api.py
    ├── app/
    ├── assignment4/
    └── screenshots/
```

## Assignment Overview

### Assignment 1 - Basic Django App
**Focus**: Django fundamentals and basic web development

- Creating Django models
- Building simple views and templates
- URL routing
- Basic database operations
- Static files management
- Admin panel usage
- Form handling

**Skills Demonstrated**:
- Model-View-Template architecture
- Database design basics
- User interface creation
- CRUD operations

---

### Assignment 2 - REST API Implementation
**Focus**: Building REST APIs with Django REST Framework

- Serializers for data validation
- ViewSets for API endpoints
- Routers for URL generation
- Authentication and permissions
- API testing with Python
- JSON request/response handling
- Error handling and status codes

**Key Features**:
- Student API endpoints
- CRUD operations via REST
- Test API script (`test_api.py`)
- Comprehensive API documentation

**Test API Usage**:
```bash
python test_api.py
```

**Skills Demonstrated**:
- REST principles
- Serialization patterns
- API design patterns
- Testing APIs programmatically

---

### Assignment 3 - Advanced Features
**Focus**: Enhanced functionality and advanced Django patterns

- Advanced querying and filtering
- Custom serializers
- Permission classes
- Advanced URL routing
- Database optimization
- Pagination and search
- Complex data relationships

**Skills Demonstrated**:
- Advanced ORM usage
- API optimization
- Complex feature implementation
- Professional API design

---

### Assignment 4 - Complex Implementation
**Focus**: Production-ready features and best practices

- Complex business logic
- Advanced permission models
- Custom authentication
- Signal handlers
- Middleware usage
- Performance optimization
- Error handling and logging

**Skills Demonstrated**:
- Production-grade code
- Complex architecture
- Scalability considerations
- Professional practices

## Common Setup Instructions

For each assignment, follow these steps:

1. Navigate to the assignment directory:
   ```bash
   cd assignmentX
   ```

2. Create and activate virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install django djangorestframework
   ```

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

5. Create superuser:
   ```bash
   python manage.py createsuperuser
   ```

6. Start development server:
   ```bash
   python manage.py runserver
   ```

7. Access application at `http://localhost:8000/`

## Testing APIs

Each REST API assignment includes a `test_api.py` script for testing:

```bash
# Run the test script
python test_api.py
```

This script demonstrates:
- POST requests for creating data
- GET requests for retrieving data
- PUT/PATCH requests for updating
- DELETE requests for removing data

## Technologies Used

- **Python 3.x**: Programming language
- **Django 3.x+**: Web framework
- **Django REST Framework**: REST API toolkit
- **SQLite3**: Database
- **HTML/CSS**: Frontend markup and styling
- **Requests**: HTTP client library for testing

## Key Learning Paths

### Progression Through Assignments

1. **Assignment 1**: Learn Django basics and MVC architecture
2. **Assignment 2**: Master REST API development
3. **Assignment 3**: Implement advanced features and optimization
4. **Assignment 4**: Build production-grade applications

## Common API Endpoints Pattern

For REST API assignments:
- `GET /api/resource/` - List all resources
- `POST /api/resource/` - Create new resource
- `GET /api/resource/<id>/` - Retrieve specific resource
- `PUT /api/resource/<id>/` - Update resource
- `PATCH /api/resource/<id>/` - Partial update
- `DELETE /api/resource/<id>/` - Delete resource

## Screenshots Directory

Each assignment includes a `screenshots/` directory containing:
- Application interface screenshots
- API testing results
- Database schema diagrams
- UI/UX demonstrations

## Learning Objectives

### All Assignments
- ✓ Django web development fundamentals
- ✓ Database design and management
- ✓ REST API principles and implementation
- ✓ Professional code organization
- ✓ Testing and debugging techniques
- ✓ Security and performance considerations
- ✓ Best practices in web development

### Specific Skills by Assignment

**Assignment 1**: Models, Views, Templates, Forms
**Assignment 2**: Serializers, ViewSets, Routers, Testing
**Assignment 3**: Advanced Queries, Permissions, Optimization
**Assignment 4**: Complex Logic, Architecture, Production-Readiness

## Notes

These assignments form a comprehensive curriculum for learning Django development:
- Start with Assignment 1 for foundational concepts
- Progress through assignments sequentially
- Each assignment builds on previous knowledge
- Include practical, real-world scenarios
- Demonstrate professional development practices

## Troubleshooting

### Migration Issues
```bash
python manage.py makemigrations
python manage.py migrate
```

### Port Already in Use
```bash
python manage.py runserver 8001
```

### Static Files Issues
```bash
python manage.py collectstatic
```

### Clear Database
```bash
rm db.sqlite3
python manage.py migrate
```

## Best Practices Learned

- Clean code organization
- DRY (Don't Repeat Yourself) principle
- Proper error handling
- Security considerations
- Performance optimization
- API documentation
- Testing strategies
- Version control practices

---

**Complete all assignments sequentially for maximum learning benefit.**
