from unittest import mock

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from src.apps.short_url.tests.factories import ShortURLFactory


class ShorURLViewSetTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.valid_data = {"name": "Name", "url": "https://example.com/"}

    def _setup_fixtures(self):
        self.short_url = ShortURLFactory()

    def setUp(self):
        self._setup_fixtures()

        self.url_list = reverse("short_url:short-urls-list")
        self.url_detail = reverse(
            "short_url:short-urls-detail", args=(self.short_url.url_squid,)
        )

    def test_list_shortened_urls(self):
        response = self.client.get(self.url_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_shortened_url(self):
        response = self.client.get(self.url_detail)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], self.short_url.id)

    @mock.patch("src.apps.short_url.views.create_short_url")
    def test_create_shortened_url(self, create_short_url_mock):
        response = self.client.post(self.url_list, self.valid_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        create_short_url_mock.delay.assert_called()

    @mock.patch("src.apps.short_url.views.create_short_url")
    def test_create_shortened_url_existing_url(self, create_short_url_mock):
        response = self.client.post(
            self.url_list, {"name": "Name", "url": self.short_url.url}
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIsNotNone(response.data.get("url"))
        create_short_url_mock.delay.assert_not_called()

    @mock.patch("src.apps.short_url.views.update_short_url")
    def test_update_shortened_url(self, update_short_url_mock):
        update_data = {"name": "new", "url": "https://new.com/"}
        response = self.client.patch(self.url_detail, update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        update_short_url_mock.delay.assert_called_with(
            url_squid=self.short_url.url_squid,
            name=update_data["name"],
            url=update_data["url"],
        )

    @mock.patch("src.apps.short_url.views.delete_short_url")
    def test_destroy_shortened_url(self, delete_short_url_mock):
        response = self.client.delete(self.url_detail)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        delete_short_url_mock.delay.assert_called_with(
            url_squid=self.short_url.url_squid
        )
