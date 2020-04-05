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
python task.py local.install.folders
python task.py local.install.setenvironment development
```


### Create docker container

```
python task.py local.docker-compose.rebuild
```


### Install Javascript Ecosystem with NPM

```
python task.py local.node.npm install
```


### Install Django

```
python task.py local.django.migrate
python task.py local.django.createsuperuser
python task.py local.django.loadexampledata
```


### Compiles and hot-reloads for development

```
python task.py local.docker-compose.serve
```

### Quick installation for development

This command can be used to skip all previously specified installation commands. djangoVue is installed in development mode and started after successful installation.

```
python task.py local.install.quickinstallation
```

## Development links

A local nginx webserver will provide the data for the development mode. The listed links are now available.
```
http://localhost
http://localhost/api/
http://localhost/admin/
```


## Useful invoke commands
A list of all implemented invoke commands.

```
python task.py --list
```

### Compiling and minifying Vue files for production
```
python task.py local.node.build
python task.py local.django.collectionstatic
```

### Start and stop of all docker containers

Start and stop the docker compose components and check the website.
```
python task.py local.docker-compose.start
python task.py local.docker-compose.stop
```



### Create a new Secret Key

With this command you can create a new `SECRET_KEY` for the `fabric/settings.json` file. Do not forget to update the environment variables after entering the setting.

```
python task.py local.django.generateSecretKey
```
