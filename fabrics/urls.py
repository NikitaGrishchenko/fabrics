from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from .views import HomeView, MapView

urlpatterns = ([
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path('user/', include('user.urls'), name="users"),
    path('cloth/', include('cloth.urls'), name="cloth"),
    path('showroom/', include('showroom.urls'), name="showroom"),
    path("map/", MapView.as_view(), name="map"),
    path("", HomeView.as_view(), name="home"),

]) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
