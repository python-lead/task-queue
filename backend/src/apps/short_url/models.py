from urllib.parse import urlparse

from django.conf import settings
from django.db import models

from src.apps.short_url.utils import get_url_squid


class ShortURL(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=32, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    url = models.URLField(max_length=256, unique=True)
    url_squid = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return f"ShortURL: {self.url_squid}"

    @property
    def short_url(self):
        return f"{urlparse(settings.BACKEND_HOST).geturl()}/{self.url_squid}/"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.url_squid:
            self.url_squid = self._generate_unique_squid()
            self.save()

    def _generate_unique_squid(self):
        squid = get_url_squid(pk=self.id)
        while ShortURL.objects.filter(url_squid=squid).exists():
            squid = get_url_squid(pk=self.id)

        return squid
