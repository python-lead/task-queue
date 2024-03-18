from celery import shared_task
from src.apps.short_url.services import ShortURLDjangoModel


@shared_task
def create_short_url(name: str, url: str):
    service = ShortURLDjangoModel()
    service.create(name=name, url=url)


@shared_task
def update_short_url(url_squid: str, name: str, url: str):
    service = ShortURLDjangoModel()
    service.update(url_squid=url_squid, name=name, url=url)


@shared_task
def delete_short_url(url_squid: str):
    service = ShortURLDjangoModel()
    service.delete(url_squid=url_squid)
