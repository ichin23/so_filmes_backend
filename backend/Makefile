export PYTHONPATH := $(PWD)

.PHONY: test test-cov lint format typecheck run

test:
	pytest -v

# test-cov:
# 	pytest --cov=sofilmes --cov-report=term-missing -v

test-cov:
	coverage run -m pytest
	coverage report -m
	coverage html

lint:
	black sofilmes tests --check

format:
	black sofilmes tests

typecheck:
	mypy sofilmes --explicit-package-bases

# Alembic

alembic:
	alembic -x DOCKER_ENV=1

migrate-dev:
	alembic upgrade head

revision:
ifndef name
	$(error Você precisa rodar: make revision name=mensagem)
endif
	alembic revision --autogenerate -m "$(name)"

downgrade:
	alembic downgrade -1

run:
	uvicorn sofilmes.api.main:app --reload --host 0.0.0.0 --port 8000
	