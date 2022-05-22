from django.urls import path

from .views import (ClothShowroomListView, ClothShowroomView,
                    ConfirmationShowroom)

app_name = "showroom"

urlpatterns = [
    path("", ClothShowroomListView.as_view(), name="list"),
    path('add/', ClothShowroomView.as_view(), name='add'),
    path('confirmation/', ConfirmationShowroom.as_view(), name='confirmation'),

]
