# recipe-app-api



# Running in docker flake8:

```bash
 docker compose run --rm app sh -c "flake8"
 ```


## Create Django App

```bash
docker compose run --rm app sh -c "django-admin startproject  app ."
```


Ruunning the tests in docker:

```bash
docker compose run --rm app sh -c "python manage.py test"
```



# create a application in docker:

```bash
docker compose run --rm app sh -c "python manage.py startapp core"
```


# Testing the wait_for_db command and the flake8 command in docker:

```bash
 docker compose run --rm app sh -c "python manage.py test && flake8"
```


```bash
docker compose run --rm app sh -c "python manage.py wait_for_db && flake8"
```



 Wipe volume and restart clean:
```bash
docker compose down -v
docker compose up --build
```