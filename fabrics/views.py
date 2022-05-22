from django.shortcuts import redirect
from django.views.generic.base import TemplateView


class HomeView(TemplateView):

    template_name = "index.html"


class MapView(TemplateView):

    template_name = "pages/map.html"

    # def dispatch(self, request, *args, **kwargs):
    #     if request.user.is_staff:
    #         return redirect('/admin')
    #     return super(HomeView, self).dispatch(request, *args, **kwargs)
