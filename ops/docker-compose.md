## docker-compose.yml example
```
version: '3.0'

services:
    my_service_qwerty:
        build:
            context: ./path_has_Dockefile_for_building_my_service_1
            args:
                FOO: ${FOO}
                BAR: ${BAR}
        ports:
            - 80:80
        volumes:
            - ${SOME_PATH}/${MY_SERVICE_QWERTY_NAME}:${SOME_PATH}/${MY_SERVICE_QWERTY_NAME}
            - ${ANOTHER_PATH}/${MY_SERVICE_QWERTY_NAME}/dev:${ANOTHER_PATH}/${MY_SERVICE_QWERTY_NAME}/dev
        env_file:
            - .env
  my_service_asdf:
        ...
```

## .env example
```bash
FOO=Hello
BAR=world
```

## build example
```bash
docker-compose build
# or
docker-compose build my_service_qwerty
```

## deploy example
```bash
# start the service as a detached mode (daemon)
docker-compose up -d my_service_qwerty
# or with applying changes of Dockerfile
docker-compose build my_service_qwerty && docker-compose up -d my_service_qwerty
```
