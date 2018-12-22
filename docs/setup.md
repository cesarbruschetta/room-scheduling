# Install Local Environment

## Create virtualenvi

```bash
$ virtualenv -p /usr/bin/python3.6 room_scheduling
```

## Clone sourcer aplication

```bash
$ cd room_scheduling
$ git clone git clone https://github.com/cesarbruschetta/
```

## Install dependences in python

```bash
$ cd app
$ ../bin/pip install -r requirements.txt 
```

## Create database and root user of aplication

```bash
$ ../bin/python ./manage.py migrate
$ ../bin/python ./manage.py createsuperuser
```

## Load default data to database

```bash
$ ../bin/python ./manage.py loaddata data_roons.json
```

## Run Development Server

```bash
$ ../bin/python ./manage.py runserver 
```

## Access in you browser the URL

[http://127.0.0.1:8000/](http://127.0.0.1:8000/)
