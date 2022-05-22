from django import forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from .models import ClothShowroom

User = get_user_model()


class ClothShowroomForm(forms.ModelForm):
    """
    Форма добавления шоурума
    """

    class Meta:
        model = ClothShowroom
        fields = (
            "name",
            "image",
            "description",
        )
