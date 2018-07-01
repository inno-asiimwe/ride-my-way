#!/bin/sh

echo "Waiting on postgres ...."

while !nc -z user_db 5432; do
    sleep 0.1
done

echo "postgres started"

python manage.py run -h 0.0.0.0