# Instalar o Ambiente Local

## Criar o virtualenv

```bash
$ virtualenv -p /usr/bin/python3.6 room_scheduling
```

## Clonar o código fonte da aplicação

```bash
$ cd room_scheduling
$ git clone https://github.com/cesarbruschetta/room-scheduling
```

## Instalar as dependências do python

```bash
$ cd app
$ ../bin/pip install -r requirements.txt 
```

## Criar o banco de dados e o usuário root da aplicação

```bash
$ ../bin/python ./manage.py migrate
$ ../bin/python ./manage.py createsuperuser
```

## Carregar dados padrões no banco de dados

```bash
$ ../bin/python ./manage.py loaddata data_roons.json
```

## Executar o servidor de desenvolvimento

```bash
$ ../bin/python ./manage.py runserver 
```

## Acessar no seu navegador a URL

[http://127.0.0.1:8000/](http://127.0.0.1:8000/)
