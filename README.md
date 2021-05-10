# docker_postgres

##para ajustar o ip do banco de dados

 docker-compose up

 docker network inspect bridge

## ver o ip do container do banco de dados postgres
parar o container, ajustar o ip em config.py e subir de novo


## para criar a tabea deste schema
 docker-compose run web /usr/local/bin/python create_db.py


acessar localhost:5050 e inserir dados

## para confirmar que funcionou
docker ps

## obter o id do container
docker exec -it fae98c9e4b78 /bin/bash

su postgres

psql -U sis_web

select * from posts;

## para obter a secret key

Run that code in a python shell:

>>> import os

>>> os.urandom(24)

b'\x1d\xc6\x0f[\xed\x18\xd6:5\xe0\x0f\rG\xaf\xb4\xf4HT\xef\xc1\xf1\xa89f'

nao esquecer de remover a letra b no comeco da string


pip install psycopg2-binary

## testar localmente antes de subir o container

python3.8 app.py


