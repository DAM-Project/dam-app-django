# DAM Project's Web-application

## Clone the repository

```bash
git clone https://github.com/DAM-Project/dam-app-django

cd dam-app-django/

```

## Installation

```bash
pip install -r requirements.txt
```

## Files

```
cd dam-app-django/dam_app

ls
```

You will see three folders and one file.

```python
manage.py - command line utility to let you interact with django project

dam_app - python package, used across multiple applications.

app - the actual app that we're going to develop

hello_world - toy app to play with.
```

Customize the `hello_world/` folder (aka hello_world application) and get comfortable with Django framework.


```
$ git clone https://github.com/DAM-Project/dam-app-django.git
```


If any modules required, try these commands under project folder in terminal
```
$ pip install django
$ pip install folium
$ pip install geemap

$ pip install virtualenv
```

You also will most likely need to install the relevant npm dependencies by running:

```bash
npm i
```

In case of fresh installation, you may have to create environment first
```
###setup virtualenv for the Project
$ virtualenv venv

###activate the environment
$ source venv/bin/activate

```
## Run the app

```python
python manage.py runserver
```

Go to `localhost:8000` to check the app running.

## For Developers

### Logging

In the code, when logging, use the below format

```python
from logging import log, [logging levels]
log(level=[...logging level...], msg="Test Log")
```

## References

* <https://docs.djangoproject.com/en/3.2/intro/tutorial01/>
* <https://realpython.com/get-started-with-django-1/>
