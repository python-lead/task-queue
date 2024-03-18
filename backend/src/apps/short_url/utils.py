from django.conf import settings
from sqids import Sqids


def get_url_squid():
    return Sqids(min_length=settings.SHORT_URL_SQUID_LENGTH)
