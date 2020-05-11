# DjangoVue in Production Mode

In this file the further steps for the production on the server are explained.

### Compiling and minifying Vue files for production

First the frontend files have to be made available for production.
```
./task.py local.node.build
```

## Local testing 
Several micro services are installed on the server. The communication with an nginx is done using docker Networks. How to create a Docker Network can be read [here](#Create-a-Docker-Network)).

```
./task.py local.docker-compose.stop
./task.py test.starttest
./task.py test.stop
```

## Rsync

Rsync is used to exchange data between the local PC and the server. All settings are done in the `./settings.json` file under "production". Please specify the `REMOTE_USER` (for example: example) and `REMOTE_HOST` (for example: example.org) In the sub-dictionary "rsync_push" `local_dir`, `remote_dir` and `exclude` files are set for every single task.


### Push local files onto the server

```
./task.py local.node.build
./task.py local.django.collectstatic
./task.py production.rsync.push
```


## Create environment variables and folder structure on the server

With the settings for "production" from the file `settings.json` the environment variables are created. The created files are uploaded to the server and the required folders for djangoVue are created.

```
./task.py production.setproductionenvironment
```


### Deploy djangoVue on the server

The next steps include building the docker container on the server and providing the data from the backend django.

```
id -u username
id -g username
```

```
./task.py production.docker-compose.rebuild
./task.py production.django.migrate
./task.py production.django.createsuperuser
./task.py production.docker-compose.start
```


## Docker

### Create a Docker Network
```
docker network create --driver bridge nginx-proxy_default || true