# Test of aplication

## Run unittest

```bash
$ cd /path/to/env/room_scheduling/app
$ python manage.py test -v 2
```

## Run analyze code by pylint

```bash
$ cd /path/to/env/room_scheduling/app
$ ../bin/pylint room_scheduling/*
```

## Run analyze code by pylint

```bash
$ cd /path/to/env/room_scheduling/app
$ ../bin/pylint room_scheduling/*
```

## Run analyze code by pep8

```bash
$ cd /path/to/env/room_scheduling/app
$ ../bin/flake8 room_scheduling/*
```

* To format code to pep8 rules

`$ ./bin/autopep8 --in-place --aggressive --aggressive -r room_scheduling/`

## Run Coverage report

After wheels the unit tests execute the command below

```bash
$ cd /path/to/env/room_scheduling/app
$ ../bin/coverage html
```

The command generate a folder called `htmlcov` and you can open the `index.html` in your browser to view the report


## Analyze by Coverage

