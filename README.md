# djangoVue

With the help of Django as backend and Vue as frontend two small websites were created. Have a look at the sample pages: 
* [milena-and-her-dog.com](milena-and-her-dog.com)
* WIP: [tirolair.com](tirolair.com)

DjangoVue includes a blog and classic pages. 
The development and production mode is provided via docker. Python invoke is used for the pleasant communication with the docker container. 


## Dependencies

The following dependencies must be installed to access the docker container using invoke.

* python 3.8+
* pip install invoke
* docker
* docker-compose

## Settings

Copy the `fabric/settings.example.json` to `./settings.json` and adapt the file to your individual needs.

Settings for ***development***, ***test***, and ***production*** can be set:
Under `django` all settings for django must be made. 
`DEBUG` should be deactivated for production. 
Specify the `ALLOWED_HOSTS` of the application.
You can choose between sqlite3 and postgres for `DB`.
If necessary, specify `POSTGRES_HOST`, `POSTGRES_USER` and `POSTGRES_PASSWORD`.
Set a `SECRET_KEY` for the application or generate a new secret key (see [Useful invoke commands](#Useful-invoke-commands)).

## Useful invoke commands
A list of all implemented invoke commands.

```
./task.py 
```

## djangoVue for development

### Installation

You can use these commands to install DjangoVue locally on your computer. In order to save time and to avoid having to enter all commands individually, the command quick installation can be entered (see [Quick installation for development](#Quick-installation-for-development)). After successful installation and entering the prompts, a development server is started.

#### Create file structure and set environment variables for django and postgres

```
./task.py local.install.folders
./task.py local.install.setenvironment development
export PROJECT=milena || tirolair
```


#### Create docker container

If the `PROJECT` environment variable has been reset, the PROJECT must be rebuilt.
```
./task.py local.docker-compose.rebuild
```


#### Install Javascript Ecosystem with NPM

```
./task.py local.node.npm install
```


#### Install Django

```
./task.py local.django.migrate
./task.py local.django.createsuperuser
./task.py local.django.loadexampledata
```


#### Compiles and hot-reloads for development

```
./task.py local.docker-compose.serve
```

#### Quick installation for development

This command can be used to skip all previously specified installation commands. djangoVue is installed in development mode and started after successful installation.

```
./task.py local.install.quickinstallation
```

### Development links

A local nginx webserver will provide the data for the development mode. The listed links are now available.
```
http://localhost
http://localhost/api/
http://localhost/admin/
```

## djangoVue for local testing and production

A detailed description for the local test environment and the operation on the server is described in the file [PRODUCTION.md](PRODUCTION.md). 
