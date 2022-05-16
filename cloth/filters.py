import django_filters

from .models import Cloth


class ClothFilter(django_filters.FilterSet):

    name = django_filters.CharFilter(method="filter_by_name")
    material = django_filters.ChoiceFilter(choices=Cloth.MATERIAL)
    color = django_filters.ChoiceFilter(choices=Cloth.COLOR)

    class Meta:
        model = Cloth
        fields = ("name", "material", "color", )

    def filter_by_name(self, queryset, name, value):
        if len(value) == 6 and value.isdigit():
            return queryset.filter(article=value)
        exclude_obj = []
        for item in queryset:
            if item.name.lower().strip().find(value.lower().strip()) != -1:
                exclude_obj.append(item.id)
        return queryset.filter(pk__in=exclude_obj)
