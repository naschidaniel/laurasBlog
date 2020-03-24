# djangoVue

With the help of Django as backend and Vue as frontend a small website was created. DjangoVue includes a blog and classic pages. 
The development and production mode are provided by docker. To communicate pleasantly with dockercontainer python invoke is used. 



## Dependencies

The following dependencies must be installed to access the dokercontainer using invoke.

```
python 3.7+
pip install invoke
```


## Settings

Copy the `fabir/settings.example.json` to `fabric/settings.json` and adapt the file to your individual needs.

Settings for ***development*** and ***production*** can be set:
Under `django` all settings for django must be made. 
`DEBUG` should be deactivated for production. 
Specify the `ALLOWED_HOSTS` of the application.
You can choose between sqlite3 and postgres for `DB`.
If necessary, specify `POSTGRES_HOST`, `POSTGRES_USER` and `POSTGRES_PASSWORD`.
Set a `SECRET_KEY` for the application or generate a new secret key (see [Create a new Secret Key](#Create-a-new-Secret-Key)).


## Installation

You can use these commands to install DjangoVue locally on your computer.



### Create Docker container

```
python fabric/task.py local.rebuild
```


### Create file structure and install Javascript Ecosystem with NPM

```
python fabric/task.py local.folders development
python fabric/task.py local.npm install
```


### Install Django

```
python fabric/task.py local.migrate
python fabric/task.py local.createsuperuser
python fabric/task.py local.loadexampledata
```


### Compiles and hot-reloads for development
```
python fabric/task.py local.serve
```


## Important Links

The following important links are now available for local development.
```
http://localhost:3000
http://localhost:3000/api/
http://localhost:3000/admin/
```


### Compiling and minifying Vue files for production

A local nginx web server is started to test the functionality of the booked files. This step should always be tested before going live.

```
python fabric/task.py local.build
python fabric/task.py test.start
```



## Useful Docker commands, which are implemented in fabric

The docker commands implemented in fabric correspond to the official docker commands.


### Building Docker containers

```
python fabric/task.py local.rebuild
```

### Start and stop all Docker containers

```
python fabric/task.py local.start
python fabric/task.py local.stop
```

### Start, stop and start a single container from the docker-compose file

```
python fabric/task.py local.run %service%
```


### Create a new Secret Key

With this command you can create a new `SECRET_KEY` for the `fabric/settings.json` file.

```
python fabric/task.py local.generateSecretKey
```

### Execute a django manage.py command 

```
python fabric/task.py local.run %service%
```



## DjangoVue in Production Mode

### Create a Docker Network
```
docker network create --driver bridge --subnet 10.5.0.0/16 nginx_proxy || true