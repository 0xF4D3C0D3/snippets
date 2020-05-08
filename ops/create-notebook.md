## Dockerfile
```Dockerfile
FROM python:3.7-buster
ENV NOTEBOOK_HOME_DIR /root/notebooks
ENV JUPYTER_PORT 8081
ENV PYTHONPATH="/home/:${PYTHONPATH}"
# ENV PYTHONPATH="/home/.../workspace:${PYTHONPATH}" (template)
RUN apt update && apt install -y vim \
 && pip install notebook \
 && pip install jupyter_contrib_nbextensions \
 && jupyter contrib nbextension install --user \
 && rm -rf /var/lib/apt/lists/*
WORKDIR ${NOTEBOOK_HOME_DIR}
CMD jupyter-notebook --port=${JUPYTER_PORT} --allow-root --ip=0.0.0.0
# or CMD sleep infinity & docker exec -it ... bash
```

## cmd

### build & run
```bash
docker build . -t example_jupyter
docker run --name example_jupyter_1 --net host -d -v "/home/test":"/home" example_jupyter
```

### get token
```bash
docker logs example_jupyter
```
