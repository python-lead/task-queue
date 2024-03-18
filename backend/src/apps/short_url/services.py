from abc import ABC, abstractmethod

from src.apps.short_url.models import ShortURL


class ShortURLService(ABC):
    @abstractmethod
    def create(self, name: str, url: str):
        pass

    @abstractmethod
    def update(self, url_squid: str, name: str, url: str):
        pass

    @abstractmethod
    def delete(self, url_squid: str):
        pass


class ShortURLDjangoModel(ShortURLService):
    def __init__(self):
        self.model = ShortURL

    def create(self, name: str, url: str):
        instance = self.model(name=name, url=url)
        instance.save()
        return instance

    def update(self, url_squid: str, name: str, url: str):
        instance = self.model.objects.get(url_squid=url_squid)
        instance.name = name
        instance.url = url
        instance.save()
        return instance

    def delete(self, url_squid: str):
        instance = self.model.objects.get(url_squid=url_squid)
        instance.delete()
