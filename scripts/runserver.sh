#!/bin/sh

LOG_DIR="/data/logs"

ACCESS_LOG="${LOG_DIR}/access.log"
ERROR_LOG="${LOG_DIR}/error.log"

echo "🚀 Starting Gunicorn server for Django application..."

exec gunicorn core.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3 \
    --timeout 120 \
    --access-logfile ${ACCESS_LOG} \
    --error-logfile ${ERROR_LOG}
