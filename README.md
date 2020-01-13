# laurasBlog

# Installation of Conda Env laurasBlog
```
conda env create -f environment.yml
```

### Activate Conda Env
```
conda activate laurasBlog
```

## Django-Backend
### Install example Data
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

## Importand Links
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