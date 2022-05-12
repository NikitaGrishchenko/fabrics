from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .models import Cloth


class ClothDetailView(DetailView):
    model = Cloth
    template_name = "pages/cloth/detail.html"


class ClothListView(ListView):
    model = Cloth
    template_name = "pages/cloth/list.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['object_list'] = News.objects.all().order_by('-id')
    #     return context
