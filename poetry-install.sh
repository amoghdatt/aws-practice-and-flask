#!/bin/sh

source $HOME/.poetry/env

poetry install --no-dev

pip install --no-cache-dir psycopg2