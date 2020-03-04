# djangoVue

The website can be installed for ***local development*** with a local sqlite3 database (Part 1: Development). It also can be run in a local ***docker-compose*** file (Part 2: Docker for production).  

# Development
## Conda Env for djangoVue
```
conda env create -f environment.yml
```

### Activate Conda Env
```
conda activate djangoVue
```

## Set Development .env
```
echo "DEBUG=True" > ./djangoVue/.env
echo "DB=sqlite3" >> ./djangoVue/.env
```

## Django-Backend
### Installation of example Data
```
python manage.py migrate
python manage.py createsuperuser
python manage.py loaddata db.json
```
### Django-Backend for development
```
python manage.py runserver

```

### VueJs-Frontend
```
cd frontend
yarn install
```

### Compiles and hot-reloads for development
```
cd frontend
yarn serve
```

### Compiles and minifies for production
```
cd frontend
yarn build
```

### Lints and fixes files
```
cd frontend
yarn lint
```

## Important Links
```
http://localhost:8000
http://localhost:8000/api/
http://localhost:8000/admin/
```


# Docker
## Export a list of the conda Env
The shellscript will export the local install packages. It will be used for building the docker container.
```
sh ./deploy/update_env_list.sh
```

## Set env Variables
### For testing on a local machine
Set the environ variables in the `djangoVue` settings Folder for `development` or `production`. Use the following commands or copy the `.env.example` file.

```
cp djangoVue/.env.example djangoVue/.env
```

### For production on a server (TODO)
```
echo "ALLOWED_HOSTS=[%%%%SERVER_URL%%%%]" >> ./djangoVue/.env
....
```

## Create a Docker Network
```
docker network create --driver bridge --subnet 10.5.0.0/16 nginx_proxy || true
```

## Build Docker Containers
```
docker-compose build
```

# Edit the `djangoVue/.env` the way you like. Generate a `SECRET_KEY` for your production server.
```
docker-compose run web /bin/bash
/opt/conda/envs/djangoVue/bin/python /web/manage.py shell -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
vim /web/djangoVue/.env
#SET the new SECRET_KEY
exit
```


## Yarn Build inside the Docker Container
```
docker-compose run web /bin/bash
cd /web/frontend/
/opt/conda/envs/djangoVue/bin/yarn install
/opt/conda/envs/djangoVue/bin/yarn build
exit
```

## POSTGRES-DB DATA Init
```
## Migrate
docker-compose run web /bin/bash -c "/opt/conda/envs/djangoVue/bin/python manage.py migrate --settings=djangoVue.settings"

## Create superuser
docker-compose run web /bin/bash -c "/opt/conda/envs/djangoVue/bin/python manage.py createsuperuser --settings=djangoVue.settings"

## Import dummy-data 
docker-compose run web /bin/bash -c "/opt/conda/envs/djangoVue/bin/python manage.py loaddata db.json --settings=djangoVue.settings"
```

## Start Docker Containers
```
docker-compose up
```

### Important links for development
```
http://localhost:3000
http://localhost:3000/api/
http://localhost:3000/admin/
```
