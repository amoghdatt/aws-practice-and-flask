#!/bin/sh



apk add --no-cache make curl postgresql-dev gcc musl-dev

curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

source $HOME/.poetry/env

poetry config virtualenvs.create false

