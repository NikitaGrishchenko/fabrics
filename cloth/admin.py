from django.contrib import admin

from .models import Cloth, Supplier


@admin.register(Cloth)
class ClothAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "article",
    )


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = (
        "name",
    )
