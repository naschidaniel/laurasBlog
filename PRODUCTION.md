# DjangoVue in Production Mode

In this file the further steps for the production on the server are explained. Make sure you have made the correct settings in the `settings.json` file. No nginx service container is started in test and production mode. The application assumes that an nginx container is present in a docker network and manages requests to the server.


## DockerDaemon certificates
The certificates for the Docker Daemon must be stored on the server in the user directory under ***.docker***. After successful download, the certificates are stored under ***./fabric/cert folder***.

```
./task.py local.install.getdockercert
```

### Compiling and minifying Vue files for production

First the frontend files have to be made available for testing and production.
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

## Rsync local file to the server

Rsync is used to exchange data between the local machine and the server. All settings are done in the `./settings.json` file under "production". Please specify the `REMOTE_USER` (for example: example) and `REMOTE_HOST` (for example: example.org) In the sub-dictionary "rsync_push" `local_dir`, `remote_dir` are set for every single task, the option `exclude` and `include` are optional. For details please see the ***rsync man page***.

```
./task.py production.rsync.push
```


## Create environment variables and folder structure on the server

With the settings for "production" from the file `settings.json` the environment variables are created. The created files are uploaded to the server and the required folders for djangoVue are created.

```
./task.py production.setproductionenvironment
```


### Deploy djangoVue on the server

To ensure that all files are stored on the server as respective users, the userid and groupid must be specified for docker. The information is stored in the `settings.json` file.

```
# The command must be executed on the server in the user directory.
id -u username
id -g username
```

The next steps include building the docker container on the server and providing the data from the backend django. 
```
./task.py production.docker-compose.rebuild
./task.py production.django.migrate
./task.py production.django.createsuperuser
./task.py production.docker-compose.start
```


## Docker
Because the nginx container is located in another docker network, a network must be set up. Optionally, an nginx service could be implemented in file `docker-compose.production.yml`.

### Create a Docker Network
```
docker network create --driver bridge nginx-proxy_default || true
