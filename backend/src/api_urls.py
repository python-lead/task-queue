from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path("api-auth/", include("rest_framework.urls")),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("", include("src.apps.short_url.urls")),
    # Optional UI:
    path(
        "schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "schema/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"
    ),
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
]
