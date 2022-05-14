from django import forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from .models import FeedbackToCloth

User = get_user_model()

class FeedbackToClothForm(forms.ModelForm):
    """
    Форма отправки отзыва к ткани
    """

    class Meta:
        model = FeedbackToCloth
        fields = ("rating", "text")
