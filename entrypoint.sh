#!/bin/sh

if ["$DATABASE" = "sqlite3"]
then
    echo "Waiting for postgress..."

    while ! nc -z db 5432; do
        sleep 0.1
    done

    echo "SQLite3 started"
fi

python manage.py flush --noinput
python manage.py migrate

if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] && [ -n "$DJANGO_SUPERUSER_EMAIL" ]; then
    python manage.py createsuperuser --noinput || true
fi

python python manage.py collectstatic --noinput

exec "$@"