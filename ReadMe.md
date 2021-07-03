## Build A SAAS With Django

### Introduction

-> What is a Saas and How to build a Saas

-> Clone Project files or use your project files
```bash
# Make sure you have git installed
git clone https://github.com/Academy-Omen/django-blogx.git
```

-> Create Virtual environment
```bash
# Windows
py -3 -m venv env
# Linux and Mac
python -m venv env
```

-> Activate environment
```bash
# Windows
.\env\Scripts\activate
# Linux and Mac
source env/bin/activate
```

-> Install Requirements
```bash
pip install -r requirements.txt
```
-> Make sure project is running
```bash
python manage.py runserver
```

-> Install django tenants
```bash
pip install django-tenants
pip freeze > requirements.txt
```
### Setup [Django Tenants](https://django-tenants.readthedocs.io/en/latest/install.html)

-> Setup Middleware and Database
```py

MIDDLEWARE = [
    # add this add the top
    # django tenant middleware
    'django_tenants.middleware.main.TenantMainMiddleware',

    #........
]


# Setup Postgres database in settings.py
DATABASES = {
    'default': {
        # Tenant Engine
        'ENGINE': 'django_tenants.postgresql_backend',
        # set database name
        'NAME': 'saasy-blog',
        # set your user details
        'USER': 'admin',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'POST': '5432'
    }
}

# DATABASE ROUTER
DATABASE_ROUTERS = (
    'django_tenants.routers.TenantSyncRouter',
)

```

-> Setup SHARED_APPS and TENANT_APPS
```py
# Application definition
"""
    These app's data are stored on the public schema
"""
SHARED_APPS = [
    'django_tenants',  # mandatory
    'tenant',  # you must list the app where your tenant model resides in

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'ckeditor',
    'ckeditor_uploader',
]
"""
    These app's data are stored on their specific schemas
"""
TENANT_APPS = [
    # The following Django contrib apps must be in TENANT_APPS
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.sessions',
    'django.contrib.messages',

    # tenant-specific apps
    'blog',
]

INSTALLED_APPS = list(SHARED_APPS) + [
    app for app in TENANT_APPS if app not in SHARED_APPS
]

```
