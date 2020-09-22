SHELL=/bin/bash

help:
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST) | sort

# ------ Code style ------ #

style:  ## Run isort and black auto formatting code style in the project
	@isort -m 3 -tc -y
	@black -S -t py37 -l 79 . --exclude '/(\.git|\.venv|env|venv|build|dist)/'

style-check:  ## Check isort and black code style
	@black -S -t py37 -l 79 --check . --exclude '/(\.git|\.venv|env|venv|build|dist)/'

clean:  ## Clean python bytecodes, optimized files, cache, coverage...
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf
	@find . -name ".cache" -type d | xargs rm -rf
	@find . -name ".coverage" -type f | xargs rm -rf
	@find . -name ".pytest_cache" -type d | xargs rm -rf
	@echo 'Temporary files deleted'

# ------ Installation requirements ------ #

requirements-pip: ## Install project packages dev.
	@pip install --upgrade pip
	@pip install -r requirements/requirements_dev.txt 

requirements-prod: ## Install project packages prod
	@pip install --upgrade pip
	@pip install -r requirements/requirements.txt

# ----------- Docker ----------- #

start: ## Create image mongoDb, Python and run app. Access 0.0.0.0:5000/web/ or 0.0.0.0:5000/api/ 
	@docker-compose build
	@docker-compose up

# ----------- Run ----------- #

run: clean ## Run script. Download files
	@python download.py $(search)
