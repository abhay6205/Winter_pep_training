# Day 21 - Email Notification System

## Overview
This project demonstrates implementing an email notification system in Django. It showcases how to configure email settings, send emails asynchronously, and manage user communications through a mail application.

## Project Structure

```
Day21/
└── mailapp/                # Main Django project
    ├── app/                # Mail application
    │   ├── models.py       # Email/Notification models
    │   ├── views.py        # Email sending views
    │   ├── forms.py        # Email forms
    │   ├── tasks.py        # Async tasks (if using Celery)
    │   ├── admin.py
    │   └── ...
    ├── mailapp/            # Project settings
    │   ├── settings.py     # Email configuration
    │   ├── urls.py
    │   └── ...
    ├── templates/          # Email templates
    │   └── *.html
    ├── static/             # Static files
    ├── manage.py           # Django management script
    └── db.sqlite3          # SQLite database
```

## Key Concepts Demonstrated

- **Email Configuration**: Setting up SMTP in Django settings
- **Email Sending**: Using Django's email backend
- **Email Templates**: HTML email templates
- **Async Tasks**: Background email sending (if Celery configured)
- **Email Validation**: Validating email addresses
- **Error Handling**: Managing email delivery failures
- **Logging**: Tracking email sending operations
- **User Communication**: Notification system implementation

## Features

- **Send Emails**: Send emails from the application
- **Email Templates**: Professional HTML email templates
- **Recipient Management**: Manage email recipients
- **Async Sending**: Background email processing
- **Email Logging**: Track sent emails
- **Error Notifications**: Alert users of sending failures
- **User Preferences**: Email opt-in/opt-out options
- **Bulk Sending**: Send emails to multiple recipients

## Setup and Installation

1. Navigate to the project directory:
   ```bash
   cd Day21/mailapp
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

4. Configure email settings in `settings.py`:
   ```python
   # For Gmail SMTP
   EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
   EMAIL_HOST = 'smtp.gmail.com'
   EMAIL_PORT = 587
   EMAIL_USE_TLS = True
   EMAIL_HOST_USER = 'your-email@gmail.com'
   EMAIL_HOST_PASSWORD = 'your-password'
   DEFAULT_FROM_EMAIL = 'your-email@gmail.com'
   ```

   OR for Console backend (testing):
   ```python
   EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
   ```

5. Apply migrations:
   ```bash
   python manage.py migrate
   ```

6. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

7. Start the development server:
   ```bash
   python manage.py runserver
   ```

8. Access the application at `http://localhost:8000/`

## Technologies Used

- **Python 3.x**: Programming language
- **Django 3.x+**: Web framework
- **SMTP Protocol**: Email sending protocol
- **Celery** (optional): Asynchronous task queue
- **Redis** (optional): Message broker for Celery
- **HTML/CSS**: Email template styling

## Email Configuration Options

### Gmail SMTP
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'app-password'  # Use app-specific password
```

### Console Backend (Development)
```python
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

### File Backend (Development)
```python
EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = os.path.join(BASE_DIR, 'sent_emails')
```

## Sending Email Examples

### Simple Email
```python
from django.core.mail import send_mail

send_mail(
    'Subject here',
    'Here is the message.',
    'from@example.com',
    ['to@example.com'],
    fail_silently=False,
)
```

### HTML Email
```python
from django.core.mail import EmailMultiAlternatives

msg = EmailMultiAlternatives(
    subject='Subject',
    body='Plain text version',
    from_email='from@example.com',
    to=['to@example.com']
)
msg.attach_alternative('<h1>HTML version</h1>', 'text/html')
msg.send()
```

## Learning Objectives

- ✓ Understanding email configuration in Django
- ✓ Implementing SMTP-based email sending
- ✓ Creating email templates
- ✓ Handling email sending errors
- ✓ Async email processing with Celery
- ✓ Email logging and tracking
- ✓ User notification system
- ✓ Email validation and verification

## Common Email Providers

| Provider | SMTP Host | Port | TLS |
|----------|-----------|------|-----|
| Gmail | smtp.gmail.com | 587 | Yes |
| Outlook | smtp-mail.outlook.com | 587 | Yes |
| SendGrid | smtp.sendgrid.net | 587 | Yes |
| Mailgun | smtp.mailgun.org | 587 | Yes |

## Important Notes

- **Security**: Never commit sensitive credentials to version control
- **App Passwords**: Use app-specific passwords for Gmail instead of account password
- **Rate Limiting**: Be aware of email sending rate limits
- **Testing**: Use console backend for development
- **Production**: Configure proper SMTP for production
- **Templates**: Use template context to personalize emails

## Notes

This project demonstrates professional email handling in Django applications, essential for user communication, notifications, and automated messaging systems.
