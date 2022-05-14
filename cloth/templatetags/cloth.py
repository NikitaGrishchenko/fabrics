from django import template

from ..models import Favourites

register = template.Library()


@register.inclusion_tag("components/favourites.html")
def favourites(pk_user) -> dict:
    favourites = Favourites.objects.filter(user_id=pk_user).order_by('-date_created')
    return {
        "object_list": favourites,
    }
