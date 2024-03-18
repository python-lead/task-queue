.PHONY: build-dev dev exec-backend clean load-local-fixtures test-backend

DEVELOPMENT-FIXTURES=fixtures/development/shortened_urls.json


build-dev:
	docker-compose build

dev:
	docker-compose up

exec-backend:
	docker exec -it tq-backend bash

clean:
	docker exec tq-backend bash -c "isort --profile black src/ && black src/"

load-local-fixtures:
	docker exec tq-backend bash -c "./manage.py loaddata $(DEVELOPMENT-FIXTURES)"

test-backend:
	docker exec tq-backend bash -c "./manage.py test"
