#!/bin/sh

echo "Waiting for PostgreSQL..."

until pg_isready \
    -h "$POSTGRES_HOST" \
    -p "$POSTGRES_PORT" \
    -U "$POSTGRES_USER"
do
    sleep 2
done

echo "PostgreSQL is ready."

python manage.py migrate

python manage.py collectstatic --noinput

exec "$@"
