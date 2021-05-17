# Simple REST Service

Example of a simple REST service.


## Development Setup
Install Requirements:

``` bash
$ vagrant up
$ vagrant ssh
$ cd /vagrant
$ python -m venv ~/env
$ source ~/env/bin/activate
$ pip install -r requirements.txt
```

Creating Django superuser

``` bash
$ python manage.py createsuperuser
$ Email: <email>
$ Name: <name>
$ Password: <password>
$ Password (again): <password>
```

Migrating models (venv)

``` bash
$ python manage.py makemigrations profile_api
$ python manage.py migrate
```

Run application (venv)

``` bash
$ python manage.py runserver 0.0.0.0:8000
```

Integration tests

``` bash
$ python -m pytest intergration_tests/*.py
```


