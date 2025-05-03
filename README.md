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

