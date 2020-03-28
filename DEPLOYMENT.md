# DjangoVue in Production Mode

In this file the further steps for the deployment on the server are explained.

## Rsync
Rsync is used to exchange data between the local PC and the server. All settings are done in the `fabric/settings.json` file under "deployment". Please specify the `remote_user` (for example: example) and `remote_host` (for example: example.org) In the sub-dictionary "rsync" `local_dir`, `remote_dir` and `exclude` files are set for every single task.

### Push local files onto the server
```
python fabric/task.py remote.push
```

## Docker

### Create a Docker Network
```
docker network create --driver bridge --subnet 10.5.0.0/16 nginx_proxy || true