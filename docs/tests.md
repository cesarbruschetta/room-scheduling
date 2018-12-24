# Teste da aplicação

## Executar unittest

```bash
$ cd /path/to/env/room_scheduling/app
$ python manage.py test -v 2
```

## Analisar o código pelo pylint

```bash
$ cd /path/to/env/room_scheduling/app
$ ../bin/pylint room_scheduling/*
```

## Analisar o código pelo pep8

```bash
$ cd /path/to/env/room_scheduling/app
$ ../bin/flake8 room_scheduling/*
```

* Formatar o codigo pelo padrão do pep8

`$ ./bin/autopep8 --in-place --aggressive --aggressive -r room_scheduling/`

## Executar o Coverage report

Após executar todos os testes unitários execute o comando abaixo

```bash
$ cd /path/to/env/room_scheduling/app
$ ../bin/coverage html
```

O comando gerará uma pasta chamada `htmlcov` e ao abri-lá irá localizar e abrir o arquivo `index.html` com seu navegador para ver o relatório


## Analise pelo Coverage

|Module|statements|missing|excluded|coverage|
|--- |--- |--- |--- |--- |
|Total|188|63|0|66%|
|Total|188|63|0|66%|
|room_scheduling/__init__.py|0|0|0|100%|
|room_scheduling/core/__init__.py|0|0|0|100%|
|room_scheduling/core/admin.py|10|10|0|0%|
|room_scheduling/core/apps.py|3|3|0|0%|
|room_scheduling/core/migrations/0001_initial.py|6|0|0|100%|
|room_scheduling/core/migrations/__init__.py|0|0|0|100%|
|room_scheduling/core/models.py|25|22|0|12%|
|room_scheduling/core/serializers.py|24|0|0|100%|
|room_scheduling/core/tests.py|62|0|0|100%|
|room_scheduling/core/urls.py|7|0|0|100%|
|room_scheduling/core/views.py|19|0|0|100%|
|room_scheduling/settings.py|24|24|0|0%|
|room_scheduling/urls.py|4|0|0|100%|
|room_scheduling/wsgi.py|4|4|0|0%|
