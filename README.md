# djangoVue

With the help of Django as backend and Vue as frontend a small website was created. DjangoVue includes a blog and classic pages. 
The development and production mode are provided by docker. To communicate pleasantly with docker container python invoke is used. 



## Dependencies

The following dependencies must be installed to access the docker container using invoke.

```
python 3.7+
pip install invoke
```


## Settings

Copy the `fabric/settings.example.json` to `fabric/settings.json` and adapt the file to your individual needs.

Settings for ***development*** and ***production*** can be set:
Under `django` all settings for django must be made. 
`DEBUG` should be deactivated for production. 
Specify the `ALLOWED_HOSTS` of the application.
You can choose between sqlite3 and postgres for `DB`.
If necessary, specify `POSTGRES_HOST`, `POSTGRES_USER` and `POSTGRES_PASSWORD`.
Set a `SECRET_KEY` for the application or generate a new secret key (see [Create a new Secret Key](#Create-a-new-Secret-Key)).


## Installation

You can use these commands to install DjangoVue locally on your computer. In order to save time and to avoid having to enter all commands individually, the command quick installation can be entered (see [Quick installation for development](#Quick-installation-for-development)). After successful installation and entering the prompts, a development server is started.

### Create file structure and set environment variables for django and postgres

```
python fabric/task.py local.folders development
python fabric/task.py local.setenvironment development
```


### Create docker container

```
python fabric/task.py local.rebuild
```


### Install Javascript Ecosystem with NPM

```
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

### Quick installation for development

This command can be used to skip all previously specified installation commands. djangoVue is installed in development mode and started after successful installation.

```
python fabric/task.py local.quickinstallation
```

## Development links

A local nginx webserver will provide the data for the development mode. The listed links are now available.
```
http://localhost
http://localhost/api/
http://localhost/admin/
```


### Compiling and minifying Vue files for production

This step should always be tested before going live. Start and stop the docker compose components and check the website.

```
python fabric/task.py local.start
python fabric/task.py local.stop
```



## Useful docker commands, which are implemented in fabric

The docker commands implemented in fabric correspond to the official docker commands.


### Build or hard rebuild of docker containers

```
python fabric/task.py local.rebuild
python fabric/task.py local.rebuildhard
```

### Start, stop, restart and fullrestart of all docker containers

```
python fabric/task.py local.start
python fabric/task.py local.stop

python fabric/task.py local.restart
python fabric/task.py local.fullrestart
```

### Start, stop and start a single container from the docker-compose file

```
python fabric/task.py local.run %service%
```

### Output logs from a single docker Container from the docker-compose file

```
python fabric/task.py local.log %service%
```

### Create a new Secret Key

With this command you can create a new `SECRET_KEY` for the `fabric/settings.json` file. Do not forget to update the environment variables after entering the setting.

```
python fabric/task.py local.generateSecretKey
python fabric/task.py local.setenvironment development #or production
```

### Execute a django manage.py command 

```
python fabric/task.py local.managepy %command%
```

### Execute a npm command 

```
python fabric/task.py local.npm %command%
```

### Serve a development server 

```
python fabric/task.py local.serve
```
