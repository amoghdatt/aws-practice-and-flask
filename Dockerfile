FROM python:3.7.9-alpine

COPY install-packages.sh .
RUN ./install-packages.sh
    
ARG PROJECT_DIR=/snakeeyes
ENV PIP_NO_CACHE_DIR=off

WORKDIR ${PROJECT_DIR}

COPY pyproject.toml poetry.lock poetry-install.sh ./
RUN ./poetry-install.sh

COPY . .

CMD gunicorn -b 0.0.0.0:8000 --access-logfile - "snakeeyes.app:create_app()"