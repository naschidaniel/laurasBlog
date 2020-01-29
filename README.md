# djangoVue

# Conda Env for djangoVue
```
conda env create -f environment.yml
```

### Activate Conda Env
```
conda activate djangoVue
```

## Django-Backend
### Installation of example Data
```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py loaddata db.json
```

## VueJs-Frontend
```
cd frontend
yarn install
```

# Development

## Django-Backend
```
python manage.py runserver
```

### Importand Links
```
http://localhost:8000/api/
http://localhost:8000/admin/
```

## VueJs-Frontend

#### Compiles and hot-reloads for development
```
cd frontend
yarn serve
```

#### Compiles and minifies for production
```
cd frontend
yarn build
```

#### Lints and fixes files
```
cd frontend
yarn lint
```


# Docker
## Export a list of the conda Env
The shellscript will export the local install packages. It will be used for building the docker container.
```
sh ./deploy/update_env_list.sh
```

## Set env Variables
### For testing on a local machine
Set the environ variables in the `djangoVue` settings Folder for `development` or `production` by using the following commands.
```
echo "SERVER_NAME=localhost" >> ./djangoVue/.env
echo "ALLOWED_HOSTS=['localhost']" >> ./djangoVue/.env

# generate a new SECRET_KEY
../manage.py shell -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
echo "SECRET_KEY='%%%%STRING%%%%'" >> ./djangoVue/.env

# POSTGRESQL-DB Settings
echo "POSTGRESQL_NAME=postgres" >> ./djangoVue/.env
echo "POSTGRESQL_USER=postgres" >> ./djangoVue/.env
echo "POSTGRESQL_PASSWORD=postgres" >> ./djangoVue/.env
echo "POSTGRESQL_PORT=5432" >> ./djangoVue/.env
```

### For production on a server (TODO)
```
echo "SERVER_NAME=%%%%SERVER_NAME%%%%" >> ./djangoVue/.env
echo "ALLOWED_HOSTS=[%%%%SERVER_URL%%%%]" >> ./djangoVue/.env

....
```

## Start Docker Containers
```
docker-compose up
```


## Build Docker Containers
```
docker-compose build
```

## POSTGRES-DB DATA Init
```
## Migrate DATA
docker-compose run web -e POSTGRES_PASSWORD=mysecretpassword -d postgres

docker-compose run web /bin/bash -c "/opt/conda/envs/djangoVue/bin/python manage.py migrate --settings=djangoVue.settings_prod"

## Create Superuser
docker-compose run web /bin/bash -c "/opt/conda/envs/djangoVue/bin/python manage.py createsuperuser --settings=djangoVue.settings_prod"

## Import Test-Data 
docker-compose run web /bin/bash -c "/opt/conda/envs/djangoVue/bin/python manage.py loaddata ./db.json --settings=djangoVue.settings_prod"
```

### Important links for development
```
http://localhost:3000/api/
http://localhost:3000/admin/
```
