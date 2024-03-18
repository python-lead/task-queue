from rest_framework import serializers

from src.apps.short_url.models import ShortURL


class ShortURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortURL
        fields = (
            "id",
            "name",
            "url",
            "url_squid",
            "created_at",
            "updated_at",
            "short_url",
        )
        read_only_fields = (
            "id",
            "url_squid",
            "created_at",
            "updated_at",
            "short_url",
        )
