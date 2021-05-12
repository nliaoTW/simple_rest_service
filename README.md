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

Run application (venv)

``` bash
$ python manage.py runserver 0.0.0.0:8000
```

Migrating models (venv)

``` bash
$ python manage.py makemigrations simple_rest_api
$ python manage.py migrate
```

Integration tests

``` bash
$ pytest intergration_tests/*.py
```


