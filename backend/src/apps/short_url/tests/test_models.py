from unittest import mock

from django.conf import settings
from django.db.utils import IntegrityError
from rest_framework.test import APITestCase

from src.apps.short_url.models import ShortURL
from src.apps.short_url.tests.factories import ShortURLFactory
from src.apps.short_url.utils import get_url_squid


class ShortURLTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.model = ShortURL

    def setUp(self):
        self.short_url = ShortURLFactory()
        self.valid_data = {"name": "Name", "url": "https://example.com/"}

    def test_save_valid_instance(self):
        instance = self.model(**self.valid_data)
        instance.save()

        self.assertEqual(instance.name, self.valid_data["name"])
        self.assertEqual(instance.url, self.valid_data["url"])
        self.assertIsNotNone(instance.url_squid)
        self.assertEqual(
            instance.short_url, f"{settings.BACKEND_HOST}/{instance.url_squid}/"
        )

    def test_save_instance_with_existing_squid(self):
        instance = self.model(**self.valid_data, url_squid=self.short_url.url_squid)

        with self.assertRaises(IntegrityError):
            instance.save()

    @mock.patch("src.apps.short_url.models.get_url_squid")
    def test_save_instance_with_squid_collision(self, get_url_squid_mock):
        unique_squid = get_url_squid(id=2)
        get_url_squid_mock.side_effect = [self.short_url.url_squid, unique_squid]

        instance = self.model(**self.valid_data)
        instance.save()

        get_url_squid_mock.assert_called_with(instance.id)
        self.assertEqual(instance.url_squid, unique_squid)
