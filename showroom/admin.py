from django.contrib import admin

from .models import ClothShowroom


@admin.register(ClothShowroom)
class ClothShowroomAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "user",
    )
