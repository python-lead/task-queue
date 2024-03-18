from django.http import HttpResponseRedirect
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from src.apps.short_url.models import ShortURL
from src.apps.short_url.serializers import ShortURLSerializer
from src.apps.short_url.tasks import (
    create_short_url,
    delete_short_url,
    update_short_url,
)


class ShortURLViewSet(viewsets.ModelViewSet):
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


class ShortUrlRedirectViewSet(viewsets.GenericViewSet):
    queryset = ShortURL.objects.all()
    lookup_field = "url_squid"

    @action(detail=True, methods=["get"], url_path="redirect")
    def redirect_to_url(self, request, url_squid=None):
        """
        Enter url using browser with valid url_squid to be redirected to shortened url original page.
        Redirect won't work through API docs interface.
        """
        try:
            short_url_instance = self.get_object()
            return HttpResponseRedirect(short_url_instance.url)
        except ShortURL.DoesNotExist:
            return Response(
                {"error": "Short URL not found"}, status=status.HTTP_404_NOT_FOUND
            )
