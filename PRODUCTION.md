# DjangoVue in Production Mode

In this file the further steps for the production on the server are explained.

## Local testing 
Several micro services are installed on the server. The communication with an nginx is done using docker Networks. How to create a Docker Network can be read [here](#Create-a-Docker-Network)).

```
python task.py test.starttest
python task.py test.stop
```

## Rsync

Rsync is used to exchange data between the local PC and the server. All settings are done in the `fabric\settings.json` file under "production". Please specify the `REMOTE_USER` (for example: example) and `REMOTE_HOST` (for example: example.org) In the sub-dictionary "rsync" `local_dir`, `remote_dir` and `exclude` files are set for every single task.


### Push local files onto the server

```
python task.py remote.push
```


## Create environment variables and folder structure on the server.

Using the settings and "production" from the `fabruc\settings.json` file, the environment variables are created. The created environment variables are uploaded to the server and the folder structure is created. 

```
python task.py remote.setproductionenvironment production
```


## Docker

### Create a Docker Network
```
docker network create --driver bridge --subnet 10.5.0.0/16 nginx_proxy || true