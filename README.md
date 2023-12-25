# What is this

This is the backend for my resume, its written in Django with DjangoRestFramework, 
It handles PDF export with a django template and xhtml2pdf. 

it has tests, models, serializers, views, and everything necessary to serve data from a backend.
The idea is the resume info is easily changed from the admin panel,
and then a PDF resume can be exported from the website, so both the website and the PDF are always updated,
and syncing them manually is not needed.

## Technology

Django + drf + django-filter
DB in postgresql
Django configurations for settings file
Common practice middlewares (timezones, querycount)

## setup
### Setup for development

1. Python virtual environment:   
We are using poetry to manage the projects dependencies.   
   **Install Poetry** - https://python-poetry.org/docs/#installation
        

2. Get the code:    
Clone this project    
   ```
   git clone git@github.com:elam91/resume_backend.git
   ```
   

3. Install dependencies:    
enter projects directory and install dependencies using Poetry. Poetry will look for pyproject.toml file
    ```
    cd resume_backend
    poetry install
    ```
   And enter the virtual env created by Poetry:
   ```
   poetry shell
   ```
   
---
### From this point in the setup you should run the commands while you are inside the virtual env / poetry shell 

---

4. Database:    
We are currently using postgres. You need to set up a user,
   * After you have installed postgres, enter postgres cli client:    
   ```
   sudo su - postgres
   psql
   ```
   * create a database, a user and a role
    ```
    CREATE DATABASE resume_backend_db;
    CREATE USER resume_backend_user WITH PASSWORD 'resume_backend_pass';
    ALTER ROLE resume_backend_user SET client_encoding TO 'utf8';
    GRANT ALL PRIVILEGES ON DATABASE resume_backend_db TO resume_backend_user;
    ALTER ROLE resume_backend_user CREATEDB;
   ```
   * If PostgreSQL version is 15+
   ```
   \c resume_backend_db
   GRANT ALL ON SCHEMA public TO resume_backend_user;
   ```
   * to exit postgres cli:   
   `Ctrl+D`
   
     and then exit superuser shell   
   `exit`
   * Now you can migrate the data:
   ```   
   python manage.py migrate   
   ```   

5. Create a superuser for yourself to start working
    ```
    python manage.py createsuperuser 
   ```

6. Run the dev server
    ```
   python manage.py runserver
   ```
 
### tests

```bash
poetry run python manage.py test
```
## Production

Ready to run as container (see dockerfile). pushing to prod deploys to fly.io.

## Setup for use in local environment as a "black box"
e.g when you work on the frontend

```bash
docker-compose up
```
First run would be quite long because of docker building

Postgres has some issues currently with start order, so if you see errors in the logs,
just restart the compose a few times until it work


### CI
Using github actions, tests and deploy to fly.