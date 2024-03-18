<h1 align="center">
  <br>
  <br>
  URL Shortener
  <br>
</h1>

<h4 align="center">DRF based URL Shortener app</h4>

## Table of contents
* [General info](#general-info)
* [How to use](#how-to-use)
* [Technologies](#technologies)
* [Setup](#setup)
* [Other](#other)

## General info
URL Shortener app based on microservices, REST API and Celery task queue.

## How to use
URL Shortener app supports creating shortened urls that consist of following data:
```
{
    "id": <Django instance id>,
    "name": <Short name>,
    "url": <Shortened url original path>,
    "urlSquid": <unique squid>,
    "createdAt": <Shortened url creation datetime>",
    "updatedAt": <Shortened url creation datetime>",
    "shortUrl": <App redirection url>"
}
```
To interact with shortened urls use Django REST framework [API explorer](http://0.0.0.0:8001/api/short-urls/) or available API documentation views.

To create new shortened url use available HTML form or insomnia/postman client.

Accessing the app using valid shortened url `urlSquid` as resource will redirect the user to short url original path.
i.e. [localhost:8001/gbHJdmfrXB/](localhost:8001/gbHJdmfrXB/) (As long as you've loaded local fixtures).

You can also just copy shortened url `shortUrl` property and use it directly in your browser.

Creating, updating and removing shortened urls is processed using celery worker.

Check [API URLs documentation](API-URLs-documentation) to see all available API endpoints.

## API URLs documentation
- [Schema yaml download](http://localhost:8001/api/schema/)
- [API swagger-ui](http://localhost:8001/api/schema/swagger-ui/)
- [API redoc](http://localhost:8001/api/schema/redoc/)

## Technologies
#### Project environment:
* Docker: 20.10.7
* docker-compose: 1.29.2

#### Project backend service:
* Python: 3.11.7
* Django: ~4.2
* djangorestframework: ^3.15.0
* celery: ^5.3.6

#### Databases used:
* postgresql: 16
* redis: latest

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

$ make clean
# enforce isort and black rules on the backend/src
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
