from datetime import datetime

from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class ClothShowroom(models.Model):
    """
    Шоурум
    """

    name = models.CharField(max_length=255, verbose_name=_("Название"))
    image = models.ImageField(verbose_name=_("Фото"))
    description = models.CharField(max_length=350, null=True, blank=True, verbose_name=_("Описание"))
    user = models.ForeignKey(User, verbose_name=_("Пользователь"), on_delete=models.CASCADE)
    is_confirmed = models.BooleanField(_("Опубликовать?"), default=False)

    class Meta:
        verbose_name = _("Шоурум")
        verbose_name_plural = _("Шоурум")

    def __str__(self):
        return self.name

