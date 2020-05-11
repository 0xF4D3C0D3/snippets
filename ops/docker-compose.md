## example
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
