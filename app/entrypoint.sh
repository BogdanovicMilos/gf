#!/bin/sh

python3 manage.py wait_for_db
python3 manage.py makemigrations
python3 manage.py migrate

exec "$@"
