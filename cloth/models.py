from datetime import datetime

from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Supplier(models.Model):
    """
    Поставщик
    """

    DISTRICT = [
    ('cenral', 'Центральный'),
    ('northwest', 'Северо-западный'),
    ('ural', 'Уральский'),
    ('south', 'Южный'),
    ('privolzhsky', 'Приволжский'),
    ('fareastern', 'Дальневосточный'),
    ('siberian', 'Сибирский'),
]

    name = models.CharField(max_length=254, verbose_name=_("Название"))
    description = models.CharField(max_length=254, verbose_name=_("Описание"), null=True, blank=True)
    date_of_foundation = models.CharField(max_length=254, verbose_name=_("Дата основания"), null=True, blank=True)
    logo = models.ImageField(null=True, blank=True, verbose_name=_("Логотип"))
    district = models.CharField(_("Округ"), max_length=25, choices = DISTRICT)
    types_of_fabrics = models.CharField(_("Виды тканей"), max_length=254, null=True, blank=True)
    address = models.CharField(max_length=254, null=True, blank=True, verbose_name=_("Адрес"))
    phone = models.CharField(max_length=254, null=True, blank=True, verbose_name=_("Номер телефона"))
    email = models.EmailField(_("E-mail"), max_length=254, null=True, blank=True)
    link_to_the_catalog = models.URLField(_("Ссылка на каталог"), max_length=200, null=True, blank=True)
    link_to_the_site = models.URLField(_("Ссылка на сайт"), max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = _("Поставщик")
        verbose_name_plural = _("Поставщики")

    def __str__(self):
        return self.name


class Cloth(models.Model):
    """
    Ткань
    """

    MATERIAL = [
    ('Текстильные', (
            ('g1e1', 'Хлопок'),
            ('g1e2', 'Лён'),
            ('g1e3', 'Шерсть'),
            ('g1e4', 'Шёлк'),
            ('g1e5', 'Эко-кожа'),
        )
    ),
    ('Технические', (
            ('g2e1', 'Огнестойкая'),
            ('g2e2', 'Для фильтрации'),
            ('g2e3', 'Водостойкая'),
            ('g2e4', 'Обтирочная'),
            ('g2e5', 'Изоляционная'),
        )
    ),
]

    COLOR = [
    ('Без принта', (
            ('white', 'Белый'),
            ('black', 'Черный'),
            ('blue', 'Синий'),
            ('red', 'Красный'),
            ('yellow', 'Жёлтый'),
            ('green', 'Зелёный'),
            ('orange', 'Оранжевый'),
            ('gray', 'Серый'),
            ('brown', 'Коричневый'),
            ('cyan', 'Голубой'),
        )
    ),
    ('С принтом', (
            ('dots', 'Горошек'),
            ('cell', 'Клетка'),
            ('graphic', 'Графический'),
            ('floral', 'Цветочный'),
            ('strip', 'Полоска'),
            ('cartoon', 'Мультяшный'),
        )
    ),
]

    name = models.CharField(max_length=255, verbose_name=_("Название"))
    image = models.ImageField(null=False, blank=False, verbose_name=_("Фото"))
    supplier = models.ForeignKey(Supplier, verbose_name=_("Поставщик"), on_delete=models.CASCADE)
    price = models.FloatField(_("Цена"))
    material = models.CharField(_("Материал"), max_length=25, choices = MATERIAL)
    color = models.CharField(_("Цвет"), max_length=25, choices = COLOR)
    description = models.CharField(max_length=350, null=True, blank=True, verbose_name=_("Описание"))
    article = models.IntegerField(_("Артикул"), unique=True, help_text='6 уникальных цифр')

    class Meta:
        verbose_name = _("Ткань")
        verbose_name_plural = _("Ткани")

    def __str__(self):
        return self.name


class Favourites(models.Model):
    """
    Избранное
    """

    user = models.ForeignKey(User, verbose_name=_("Пользователь"), on_delete=models.CASCADE)
    cloth = models.ForeignKey(Cloth, verbose_name=_("Ткань"), on_delete=models.CASCADE)
    date_created = models.DateTimeField(_("Дата создания"), default=timezone.now)

    class Meta:
        verbose_name = _("Избранное")
        verbose_name_plural = _("Избранное")

    def __str__(self):
        return f"{self.user} {self.cloth}"


class FeedbackToCloth(models.Model):
    """
    Отзыв к ткани
    """

    user = models.ForeignKey(User, verbose_name=_("Пользователь"), on_delete=models.CASCADE)
    cloth = models.ForeignKey(Cloth, verbose_name=_("Ткань"), on_delete=models.CASCADE)
    date_created = models.DateTimeField(_("Дата создания"), default=timezone.now)
    rating = models.IntegerField(_("Рейтинг"), validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ])
    text = models.CharField(_("Текст"), max_length=300)

    class Meta:
        verbose_name = _("Отзыв к ткани")
        verbose_name_plural = _("Отзыв к ткани")

    def __str__(self):
        return f"Отзыв {self.user} к {self.cloth}"
