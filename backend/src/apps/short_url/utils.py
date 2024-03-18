from django.conf import settings
from sqids import Sqids


def get_url_squid(pk: int) -> str:
    return Sqids(min_length=settings.SHORT_URL_SQUID_LENGTH).encode([pk])
