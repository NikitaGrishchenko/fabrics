from django.urls import path

from .views import (ClothDetailView, ClothListView, SupplierDetailView,
                    SupplierListView, UserFavouritesListView, add_to_favorites,
                    delete_from_favorites, send_feedback)

app_name = "cloth"

urlpatterns = [
    path("", ClothListView.as_view(), name="list"),
    path("supplier/", SupplierListView.as_view(), name="supplier-list"),
    path("favourites/", UserFavouritesListView.as_view(), name="favourites"),
    path("<int:pk>/", ClothDetailView.as_view(), name="detail"),
    path("supplier/<int:pk>/", SupplierDetailView.as_view(), name="supplier-detail"),
    path("add-to-favorites/<int:pk>/", add_to_favorites, name="add-to-favorites"),
    path("delete-from-favorites/<int:pk>/", delete_from_favorites, name="delete-from-favorites"),
    path("send-feedback/<int:pk>/", send_feedback, name="send-feedback"),
]
