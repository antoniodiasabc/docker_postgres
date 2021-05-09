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

