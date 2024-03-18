from rest_framework.routers import DefaultRouter

from src.apps.short_url.views import ShorURLViewSet

app_name = "short_url"

router = DefaultRouter()
router.register(r"short-urls", ShorURLViewSet, basename="short-urls")

urlpatterns = router.urls
