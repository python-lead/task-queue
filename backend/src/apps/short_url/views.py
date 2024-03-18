from rest_framework import viewsets

from src.apps.short_url.models import ShortURL
from src.apps.short_url.serializers import ShortURLSerializer


class ShorURLViewSet(viewsets.ModelViewSet):
    queryset = ShortURL.objects.all()
    serializer_class = ShortURLSerializer
    lookup_field = "url_squid"
