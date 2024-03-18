from rest_framework import viewsets

from src.apps.short_url.models import ShortURL
from src.apps.short_url.serializers import ShortURLSerializer
from src.apps.short_url.tasks import (
    create_short_url,
    delete_short_url,
    update_short_url,
)


class ShorURLViewSet(viewsets.ModelViewSet):
    queryset = ShortURL.objects.all()
    serializer_class = ShortURLSerializer
    lookup_field = "url_squid"

    def perform_create(self, serializer):
        create_short_url.delay(
            name=serializer.validated_data["name"], url=serializer.validated_data["url"]
        )

    def perform_update(self, serializer):
        update_short_url.delay(
            url_squid=serializer.instance.url_squid,
            name=serializer.validated_data["name"],
            url=serializer.validated_data["url"],
        )

    def perform_destroy(self, instance):
        delete_short_url.delay(url_squid=instance.url_squid)
