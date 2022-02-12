FROM python:3.9-slim-buster

RUN pip install poetry

WORKDIR /app

COPY ./poetry.lock pyproject.toml /app/

RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

COPY gunicorn_conf.py alembic.ini scripts cli.py tests /app/

COPY ./app /app/

USER 1000

CMD ["uvicorn", "app:main:app", "--host", "0.0.0.0", "--port", "8000"]