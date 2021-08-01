## Build A SAAS With Django

### Introduction

-> What is a Saas and How to build a Saas

-> Clone Project files or use your project files

```bash
# Make sure you have git installed
git clone https://github.com/Academy-Omen/django-blogx.git
# clone with SSH
git clone git@github.com:Academy-Omen/django-blogx.git
```

-> Create Virtual environment

```bash
# Windows
py -3 -m venv env
# Linux and Mac
python3 -m venv env
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
pip install psycopg2
pip freeze > requirements.txt
```

### Setup [Django Tenants](https://django-tenants.readthedocs.io/en/latest/install.html)

-> Setup Middleware and Database. First create a PostgreSQL database and
note the user and password

```py

MIDDLEWARE = [
    # add this at the top
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
        'NAME': 'saasy',
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

-> Create tenant app

```bash
python manage.py startapp tenant
# Now go ahead and Create Tenant Models
```

-> Configure TENANT_MODEL and TENANT_DOMAIN_MODEL

```py
TENANT_MODEL = "tenant.Tenant"

TENANT_DOMAIN_MODEL = "tenant.Domain"
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

    # we place blog here since we want 
    # public schema to have the same structure like tenant apps
    'blog',
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

-> Make migrations and Apply to database

```bash
# create migrations files
python manage.py makemigrations
# You may need to run migrations for specific app
python manage.py makemigrations blog
# Apply migrations
python manage.py migrate_schemas
```

-> Setup Initial User, Tenant and Admin

```bash
# create first user
python manage.py createsuperuser
# Create the Public Schema
python manage.py create_tenant
# Create the Administrator
python manage.py create_tenant_superuser
python manage.py runserver
```

-> Create a custom middleware

```py
from django_tenants.middleware.main import TenantMainMiddleware


class TenantMiddleware(TenantMainMiddleware):
    """
    Field is_active can be used to temporary disable tenant and
    block access to their site. Modifying get_tenant method from
    TenantMiddleware allows us to check if tenant should be available
    """
    def get_tenant(self, domain_model, hostname):
        tenant = super().get_tenant(domain_model, hostname)
        if not tenant.is_active:
            raise self.TENANT_NOT_FOUND_EXCEPTION("Tenant is inactive")
        return tenant

```
-> Add the middleware
```py
    #.
    #.
    # custom tenant middleware
    'core.middleware.TenantMiddleware',
    #.
    #.
```

-> Modify Home View

```py
    #.
    #.
    hostname_without_port = remove_www(request.get_host().split(':')[0])
    domain = Domain.objects.get(domain=hostname_without_port)
    name = domain.tenant.blog_name
    print(name)
    #.
    #.
    context = {
        'name': name,
        'articles': featured
    }
```

##### For more information check the [django tenant docs](https://django-tenants.readthedocs.io/)
