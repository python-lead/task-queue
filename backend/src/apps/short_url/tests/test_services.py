from rest_framework.test import APITestCase

from src.apps.short_url.models import ShortURL
from src.apps.short_url.services import ShortURLDjangoModel
from src.apps.short_url.tests.factories import ShortURLFactory


class ShortURLDjangoModelServiceTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.service = ShortURLDjangoModel()
        cls.model = ShortURL

    def setUp(self):
        self.short_url = ShortURLFactory()
        self.valid_data = {"name": "Name", "url": "https://example.com/"}

    def test_create_short_url(self):
        self.service.create(name=self.valid_data["name"], url=self.valid_data["url"])
        instance = self.model.objects.filter(**self.valid_data).first()

        self.assertIsNotNone(instance)
        self.assertEqual(instance.name, self.valid_data["name"])
        self.assertEqual(instance.url, self.valid_data["url"])
        self.assertIsNotNone(instance.url_squid)

    def test_update_short_url(self):
        self.service.update(
            url_squid=self.short_url.url_squid,
            name=self.valid_data["name"],
            url=self.valid_data["url"],
        )
        self.short_url.refresh_from_db()

        self.assertEqual(self.short_url.name, self.valid_data["name"])
        self.assertEqual(self.short_url.url, self.valid_data["url"])
        self.assertIsNotNone(self.short_url.url_squid)

    def test_delete_short_url(self):
        self.service.delete(url_squid=self.short_url.url_squid)
        instance = self.model.objects.filter(url_squid=self.short_url.url_squid).first()

        self.assertIsNone(instance)
