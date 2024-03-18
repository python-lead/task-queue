from rest_framework.routers import DefaultRouter

from src.apps.short_url.views import ShortURLViewSet

app_name = "short_url"

router = DefaultRouter()
router.register(r"short-urls", ShortURLViewSet, basename="short-urls")

urlpatterns = router.urls
