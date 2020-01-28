# laurasBlog

# Conda Env for laurasBlog
```
conda env create -f environment.yml
```

### Activate Conda Env
```
conda activate laurasBlog
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
## For testing on a local machine
The nginx settings are different for `localhost` and the `server`. To ensure that nginx take the correct configuration, type one of the following commands.

```
echo "HOST=local" >> .env
```

## For production on a server (TODO)
```
echo "HOST=production" >> .env
```


# Export a list of current installed conda packages
Set the current working directory in the shell script and run it. The process will ensure that the local and server packages are the same.

```
sh ./deploy/update_env_list.sh
```

