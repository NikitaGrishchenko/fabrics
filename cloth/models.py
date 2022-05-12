from datetime import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _


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
    logo = models.ImageField(null=False, blank=False, verbose_name=_("Логотип"))
    district = models.CharField(_("Округ"), max_length=25, choices = DISTRICT)
    address = models.CharField(max_length=254, null=True, blank=True, verbose_name=_("Адрес"))
    phone = models.CharField(max_length=50, null=True, blank=True, verbose_name=_("Номер телефона"))
    email = models.EmailField(_("E-mail"), max_length=254)

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
