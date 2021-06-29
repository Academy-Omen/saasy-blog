## Build A SAAS With Django

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
