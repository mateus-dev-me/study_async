#!/bin/sh
makemigrations.sh
echo "⚙️ Making migrations..."
python manage.py migrate --noinput
