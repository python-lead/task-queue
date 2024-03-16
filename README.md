<h1 align="center">
  <br>
  <br>
  task-queue
  <br>
</h1>

<h4 align="center">DRF based task queue app</h4>

## Table of contents
* [Technologies](#technologies)
* [Setup](#setup)
* [Other](#other)

## Technologies
#### Project environment:
* Docker: 20.10.7
* docker-compose: 1.29.2

#### Project backend service:
* Python: 3.11.7
* Django: ~4.2

#### Databases used:
* postgresql: 16

## Requirements:
* Docker: ^24.0.2
* docker-compose: ^2.18.1

#### Optional:
* make

## Setup
### Starting app services locally:

To run this project locally `cd` into the project directory and use following make commands:

```
$ make build-dev
# Builds docker containers

$ make dev
# Starts containers for local development

$ make exec-backend
# enters backend container shell via bash
```

### Loading local development data from fixtures:

1. Ensure the backend service is running
2. Execute make file command

```
$ make load-local-fixtures
# loads local development data from backend/fixtures/development directory
```

## Other:

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
