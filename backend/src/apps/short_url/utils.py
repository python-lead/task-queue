from django.conf import settings
from sqids import Sqids


def get_squid():
    return Sqids(min_length=settings.SHORT_URL_SQUID_LENGTH)
