from django.conf import settings
from django.db import models

from src.apps.short_url.utils import get_url_squid


class ShortURL(models.Model):
    url = models.URLField(max_length=256, unique=True)
    url_squid = models.CharField(max_length=16, default=get_url_squid, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"ShortURL: {self.url_squid}"

    @property
    def short_url(self):
        return f"{settings.BACKEND_HOST}/{self.url_squid}"
