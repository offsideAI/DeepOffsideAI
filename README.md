# DeepOffsideAI

DeepOffsideAI is an agentic AI platform that enables users to build open source AI models and deploy agents

DeepOffsideAI is a SKAP Stack (SvelteKit - (fast)API - Postgres- stack) toolkit for building, testing and deploying fullstack AI plugins and applications

This project uses FastAPI and SQLModel


## Screenshots

## Steps for blog

```

==> python3 -m venv myvenv

==> source myvenv/bin/activate

pip install fastapi

pip install "uvicorn[standard]"

pip install pydantic

pip install --upgrade pip

==> python --version (should be 3.9 or higher)
Python 3.10.9

==> uvicorn --version
Running uvicorn 0.15.0 with CPython 3.10.9 on Darwin

pip install sqlalchemy

pip install passlib

pip install bcrypt

pip install sqladmin

pip install openai

```
## JWT Dependencies

```
pip install "python-jose[cryptography]"

pip install "passlib[bcrypt]"

```

## Develop backend locally

```
conda deactivate

cd app

python3 -m venv myvenv OR source myvenv/bin/activate

source myvenv/bin/activate

pip install -r app/requirements.txt
###################################

uvicorn main:app --reload
###################################
```


## Deployment

* Dockerfile https://fastapi.tiangolo.com/deployment/docker/

```
Dockerfile¶

Now in the same project directory create a file Dockerfile with:

#
FROM python:3.9

#
WORKDIR /code

#
COPY ./requirements.txt /code/requirements.txt

#
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

#
COPY ./app /code/app

#
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]

```

* Build Dockerfile

```
docker build -t codelabsprostack:0.0.1 .
```

* Run Docker Container Locally

```
docker run -p 8080:8080 --name codelabsprostack codelabsprostack:0.0.1
```

* List docker images

```
docker images -a
```


* List running docker processes

```
docker ps -a
```

* Remove running docker process

```
docker rm codelabsprostack
```

## Frontend Develop
* Frontend (web) was created using SvelteKit with the below config

```

==> npm create skeleton-app@latest web
┌  Create Skeleton App (version 0.0.29)

Welcome to Skeleton 💀! A UI tookit for Svelte + Tailwind

Problems? Open an issue on https://github.com/skeletonlabs/skeleton/issues if none exists already.
│
◇  Add type checking with TypeScript?
│  Yes, using TypeScript syntax
│
◇  Add ESLint for code linting?
│  Yes
│
◇  Add Prettier for code formatting ?
│  Yes
│
◇  Add Playwright for browser testing ?
│  No
│
◇  Add Vitest for unit testing ?
│  No
│
◇  Install component dependencies:
│  CodeBlock (installs highlight.js), Popups (installs floating-ui)
│
◇  Pick tailwind plugins to add:
│  forms, typography, line-clamp
│
◇  Select a theme:
│  Crimson
│
◇  Which Skeleton app template?
│  Bare Bones
│
◇  Done installing

Done! You can now:

cd web

###################################
npm run dev
###################################
```



## Develop local

```
cd app

npm run dev

```

## Alembic

### Alembic for migrations


* Run alembic init <alembic_folder_name>

```
pip install alembic

alembic init <alembic_migrations_folder> OR alembic init alembic

* alembic.ini
```

* Add sqlalchemy.url = postgres://codelabsprostack_admin_1:@127.0.0.1/codelabsprostack_prod_1 to line 64 of alembic.ini

OR

In env.py, load CONNECTION_STRING from .env

```
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

CONNECTION_STRING = os.environ.get("CONNECTION_STRING")
config.set_main_option('sqlalchemy.url', CONNECTION_STRING)
```


* Add sqlmodel import in script.py.mako

```
Add
import sqlmodel
below
import sqlalchemy as sa in script.py.mako
```

* env.py - In env.py
  
Below
from logging.config import fileConfig
```
from models import *
from sqlmodel import SQLModel
```

Change
```
target_metadata = None
```

to

```
target_metadata = SQLModel.metadata
```

* Alembic create migrations

```
cd app
alembic revision --autogenerate -m "Create"
```

* Alembic run migrations
```
cd app
alembic upgrade heads
```

* Alembic downgrade

```
alembic downgrade <version>
```

## Postgres Troubleshooting

```
psql postgres

postgres=# CREATE DATABASE chatoffside_dev_1;

postgres=# CREATE ROLE chatoffside_admin_1;

postgres=# GRANT ALL PRIVILEGES ON DATABASE chatoffside_dev_1 TO chatoffside_admin_1;

ALTER ROLE "chatoffside_admin_1" WITH LOGIN;

psql --host=localhost --username=my_user --dbname=my_database

==> psql --host=localhost --username=chatoffside_admin_1 --dbname=chatoffside_dev_1


psql postgres -c 'SHOW config_file'
                config_file
--------------------------------------------
 /opt/homebrew/var/postgres/postgresql.conf`


postgres=# REASSIGN OWNED BY skfaps_user TO unicorn_user;
REASSIGN OWNED
postgres=# DROP OWNED BY skfaps_user;
DROP OWNED
postgres=# DROP USER skfaps_user;
ERROR:  role "skfaps_user" cannot be dropped because some objects depend on it
DETAIL:  1 object in database skfaps_dev_1
postgres=# DROP DATABASE skfaps_dev_1;
DROP DATABASE
postgres=# DROP USER skfaps_user;
 ```

# Migrations Log

```
alembic revision --autogenerate -m "Create"

alembic revision --autogenerate -m "Added tags to Post user model"

alembic revision --autogenerate -m "Removed tags from Post user model"

alembic revision --autogenerate -m "Added Prompt dataclass to models"

alembic upgrade heads
```

## Useful Links

Alembic + SQLModel - https://www.youtube.com/watch?v=Rb4_90gG_Lc

Alembic - https://youtu.be/SdcH6IEi6nE


## Generate SECRET_KEY

openssl rand -base64 32

ee8b93f88b000896451907e0f6e7fe7b1fc62b096a3ff9b8166577eb9390150b

## PROD Start Command

```
uvicorn main:app --host 0.0.0.0 --port 10000
```
