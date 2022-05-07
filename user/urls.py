from django.urls import path

from .views import (AccountVeiw)

app_name = 'user'

urlpatterns = [
    path('account/', AccountVeiw.as_view(), name='account'),
    # path('registration/', RegistrationView.as_view(), name='registration'),
    # path("thanks/", ThanksView.as_view(), name="thanks"),
    # path("success/", SuccessView.as_view(), name="success"),
    # path("error/", ErrorView.as_view(), name="error"),
]
