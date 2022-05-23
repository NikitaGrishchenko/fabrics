from constance import config
from django.shortcuts import redirect
from django.views.generic.base import TemplateView


class HomeView(TemplateView):

    template_name = "index.html"


class MapView(TemplateView):

    template_name = "pages/map.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['config'] = config
        return context
