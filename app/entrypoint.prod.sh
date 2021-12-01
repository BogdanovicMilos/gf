#!/bin/sh

python3 manage.py wait_for_db

exec "$@"
