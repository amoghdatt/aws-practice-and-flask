FOLDER := snakeeyes
SHELL := /bin/bash

run_coverage:
	@docker-compose exec website pytest --cov-report term-missing --cov $(FOLDER)
run_test:
	@docker-compose exec website pytest -v
flake8:
	@flake8 $(FOLDER) --exclude __init__.py


