.PHONY: build-dev dev exec-backend clean load-local-fixtures

DEVELOPMENT-FIXTURES=fixtures/development/users.json


build-dev:
	docker-compose build

dev:
	docker-compose up

exec-backend:
	docker exec -it tq-backend bash

clean:
	isort --profile black backend/src/ && black backend/src/

load-local-fixtures:
	docker exec tq-backend bash -c "./manage.py loaddata $(DEVELOPMENT-FIXTURES)"
