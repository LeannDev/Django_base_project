# Django Base Project

**Django_base_project** is a base Django setup designed to streamline the creation of new Django projects. It comes with commonly used apps and features preconfigured, so you don't need to start from scratch every time.

## Features

- Custom user model
- User profiles
- Email verification
- Password reset and change
- Profile editing
- Email sending system
- Ready for branding and multi-environment setups

## Requirements

- Python 3.10 or higher
- SQLite for development (PostgreSQL planned for production)
- Virtual environment (recommended)

## Getting Started

### 1. Clone the Repository

```bash
    git clone https://github.com/yourusername/Django_base_project.git
    cd Django_base_project
```

### 2. Create and Activate a Virtual Environment
```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
```
### 3. Install Dependencies
```bash
    pip install -r requirements.txt
```
### 4. Create a *.env* File
Create a **.env** file in the root directory with the following variables:

```bash
    # Django settings
    SECRET_KEY=your-secret-key
    DEBUG=True

    # Encryption key for sensitive data
    ENCRYPTION_KEY=your-encryption-key

    # Branding
    CURRENT_SITE=mywebsite.com
    BRAND=YourBrand
    SLOGAN=YourSlogan

    # Email settings
    EMAIL_HOST=smtp.your-email.com
    EMAIL_PORT=587
    EMAIL_USE_TLS=True
    EMAIL_HOST_USER=your@email.com
    EMAIL_HOST_PASSWORD=your-email-password
```
### 5. Apply Migrations
Run migrations one app at a time as follows:
```bash
    python manage.py makemigrations users
    python manage.py migrate users

    python manage.py makemigrations emails
    python manage.py migrate emails

    python manage.py makemigrations images
    python manage.py migrate images

    python manage.py makemigrations profiles
    python manage.py migrate profiles

    # Migrate default Django apps
    python manage.py migrate
```
### 6. Create a Superuser
```bash
    python manage.py createsuperuser
```

### 7. Run the Development Server
```bash
    python manage.py runserver
```