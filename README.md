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
The nginx settings are different for `localhost` and `production`. Set the enviroment variables by using the following commands.
```
echo "HOST=local" >> .env
```

### For production on a server (TODO)
```
echo "HOST=production" >> .env
```

## Build Docker Containers
```
docker-compose build
```

## Start Docker Containers
```
docker-compose up
```

### Importand Links
```
http://localhost:3000/api/
http://localhost:3000/admin/
```
