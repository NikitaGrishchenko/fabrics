from django.urls import path

from .views import ClothDetailView, ClothListView

app_name = "cloth"

urlpatterns = [
    path("", ClothListView.as_view(), name="list"),
    path("<int:pk>/", ClothDetailView.as_view(), name="detail"),
]
