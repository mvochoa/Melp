# Melp

Prueba Back-end Developer Intelimétrica [Demo](https://fastapi-mario.herokuapp.com/)

Enlaces de la documentación de la API Rest:

- Postman: [https://www.postman.com/mvochoaa/workspace/melp-intelimtrica/overview](https://www.postman.com/mvochoaa/workspace/melp-intelimtrica/overview)
- Swagger UI: [https://fastapi-mario.herokuapp.com/docs](https://fastapi-mario.herokuapp.com/docs)
- ReDoc: [https://fastapi-mario.herokuapp.com/redoc](https://fastapi-mario.herokuapp.com/redoc)

## Desarrollo

Para correr el sistema solo es necesario levantar los contenedores de docker, usando el comando:

```sh
$ docker-compose up -d
```

Esto va a levantar la api en [http://localhost:8000/](http://localhost:8000/). Si se quiere probar la api y ver las documentación se puede ver en las rutas:

- Swagger UI [http://localhost:8000/docs](http://localhost:8000/docs): Esta ruta permite probar las diferentes rutas de la api, directamente en el navegador.
- ReDoc [http://localhost:8000/redoc](http://localhost:8000/redoc)

### Migraciones

Los archivos de las migraciones se encuentran en la carpeta `src/alembic/versions`. Para crear nuevos archivos de migraciones y ejecutarlos se necesita correr los comandos:

```sh
$ docker-compose exec app sh
/var/app $ alembic revision -m "create account table"
/var/app $ alembic upgrade head
```

### Pruebas

Los archivos de las pruebas se encuentran en la carpeta `src/tests`. Para ejecutar las prebas es necesario correr los comandos:

```sh
$ docker-compose exec app sh
/var/app $ pytest -vv -x
```