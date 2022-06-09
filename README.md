# quadratic_equation

## DESCRIPTION
API service calculating quadratic equations. After calculating results
write in database.

## ENDPOINTS

### GET INFORMATION
Calculate with certain parameters.

 `/api/v1/answer/?a=1&b=2&c=3`  `POST`

*Request parameters*

query - a, b, c;

a - float

b - float

c - float

*Request response (sample)*
```json
{
    "id": 7,
    "coefficient_1": 0.0,  (a)
    "coefficient_2": 0.0,  (b)
    "coefficient_3": 6.0,  (c)
    "root_1": null,
    "root_2": null,
    "answer": "Not roots"
}
```
*Responses*

200-OK

## PROGRAMMING LANGUAGE

- Python 3.8

## TECHNOLOGY

- Django 2.2
- DRF 3.12
- Docker, docker-compose

## DATABASE

- SQLite (Default)
- PostgreSQL 12.11

## HOW TO START PROJECT

- Clone repository and going:
```bash
git clone ...
```

### With docker (with PostgreSQL)

- Create .env file, define names: DB_ENGINE, DB_USERNAME, DB_PASSWORD, DB_DATABASE, DB_HOST, DB_PORT

example:

DB_ENGINE=django.db.backends.postgresql etc

- Deploy app:
```bash
sudo docker-compose up -d --build
```

- Make migrations:
```bash
docker-compose exec web python quadratic_equation/manage.py migrate
```
- Reboot app:
```bash
docker-compose stop
docker-compose start
```

### OPTIONS

host: localhost

port: 8000

### Without docker (with SQLite)

- Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
```

-Install dependencies from file requirements.txt:
```bash
pip install -r requirements.txt
```

-Make migrations:
```bash
python manage.py migrate
```

-Run project:
```bash
python manage.py runserver
```

# AUTHORS
*Kozhevnikov Aleksei*
