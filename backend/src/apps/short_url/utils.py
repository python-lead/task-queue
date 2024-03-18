from django.conf import settings
from sqids import Sqids


def get_url_squid(id: int):
    return Sqids(min_length=settings.SHORT_URL_SQUID_LENGTH).encode([id])
