# Day 19 - Django REST API Practice Project

## Overview
This project demonstrates building a comprehensive REST API using Django and Django REST Framework. It showcases API design patterns, serialization, viewsets, and best practices for creating production-ready APIs.

## Project Structure

```
Day19/
└── practice/               # Main Django project
    ├── todo_app/           # Todo REST application
    │   ├── models.py
    │   ├── views.py
    │   ├── serializers.py
    │   ├── urls.py
    │   ├── admin.py
    │   └── ...
    ├── todo_project/       # Project settings
    │   ├── settings.py
    │   ├── urls.py
    │   ├── wsgi.py
    │   └── ...
    ├── manage.py           # Django management script
    ├── requirements.txt    # Project dependencies
    └── db.sqlite3          # SQLite database
```

## Key Concepts Demonstrated

- **Django REST Framework**: Building RESTful APIs
- **Serializers**: Converting Django models to JSON
- **ViewSets**: Automated API endpoint generation
- **Routers**: URL routing for API endpoints
- **Authentication**: API authentication mechanisms
- **Permissions**: Access control for API endpoints
- **Pagination**: Handling large datasets
- **Filtering & Search**: API filtering capabilities
- **Error Handling**: Proper HTTP status codes and error responses

## Features

- **REST Endpoints**: Full CRUD REST API endpoints
- **JSON Serialization**: Proper JSON request/response handling
- **Viewsets**: Automated view generation for models
- **Routers**: Clean URL routing
- **API Documentation**: Browsable API interface
- **Authentication**: Request authentication
- **Pagination**: Result pagination
- **Filtering**: Query parameter filtering
- **Search**: Full-text search capabilities

## Setup and Installation

1. Navigate to the project directory:
   ```bash
   cd Day19/practice
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
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

7. Access the API at `http://localhost:8000/api/`

8. Access admin panel at `http://localhost:8000/admin/`

## Technologies Used

- **Python 3.x**: Programming language
- **Django 3.x+**: Web framework
- **Django REST Framework**: REST API toolkit
- **SQLite3**: Database
- **Requests**: HTTP client library

## API Endpoints

### Todo Endpoints
- `GET /api/todos/` - List all todos
- `POST /api/todos/` - Create new todo
- `GET /api/todos/<id>/` - Retrieve specific todo
- `PUT /api/todos/<id>/` - Update todo
- `PATCH /api/todos/<id>/` - Partial update
- `DELETE /api/todos/<id>/` - Delete todo

## Requirements

The `requirements.txt` file includes:
```
django
djangorestframework
psycopg2-binary  # For PostgreSQL support (optional)
```

## API Request Examples

### Create a Todo
```bash
curl -X POST http://localhost:8000/api/todos/ \
  -H "Content-Type: application/json" \
  -d '{"title": "My Todo", "description": "Description here"}'
```

### Get All Todos
```bash
curl http://localhost:8000/api/todos/
```

### Update a Todo
```bash
curl -X PUT http://localhost:8000/api/todos/1/ \
  -H "Content-Type: application/json" \
  -d '{"title": "Updated Todo", "description": "Updated description"}'
```

### Delete a Todo
```bash
curl -X DELETE http://localhost:8000/api/todos/1/
```

## Learning Objectives

- ✓ Understanding REST API principles
- ✓ Building APIs with Django REST Framework
- ✓ Implementing serializers for data validation
- ✓ Using ViewSets for rapid API development
- ✓ Proper URL routing with routers
- ✓ Authentication and permission handling
- ✓ Pagination and filtering
- ✓ Error handling and status codes
- ✓ API documentation and testing

## Authentication (if implemented)

- Token-based authentication
- Session-based authentication
- Custom permission classes

## Testing

API endpoints can be tested using:
- **Postman**: GUI-based API testing
- **curl**: Command-line HTTP client
- **Python requests**: Programmatic testing
- **Django test framework**: Unit testing

## Notes

This practice project provides hands-on experience with building production-grade REST APIs using Django REST Framework, demonstrating patterns and best practices for API development.
