FROM python:3.11.3-alpine3.18

LABEL mantainer="mateus-dev-me.com.br"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY ./app /app
COPY ./scripts /scripts

WORKDIR /app

EXPOSE 8000

RUN python -m venv /venv && \
  /venv/bin/pip install --upgrade pip && \
  /venv/bin/pip install -r /app/requirements.txt && \
  adduser --disabled-password --no-create-home appuser && \
  mkdir -p /data/web/static && \
  mkdir -p /data/web/media && \
  mkdir -p /data/logs && \
  chown -R appuser:appuser /venv && \
  chown -R appuser:appuser /data/web/static && \
  chown -R appuser:appuser /data/web/media && \
  chown -R appuser:appuser /data/logs && \
  chmod -R 755 /data/web/static && \
  chmod -R 755 /data/web/media && \
  chmod -R 755 /data/logs && \
  chmod -R +x /scripts


ENV PATH="/scripts:/venv/bin:$PATH"

USER appuser

CMD ["commands.sh"]
