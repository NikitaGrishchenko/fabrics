from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .models import Cloth, Favourites


class ClothDetailView(DetailView):
    model = Cloth
    template_name = "pages/cloth/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = Cloth.objects.get(id=self.kwargs['pk'])
        try:
            is_favourites = Favourites.objects.get(
                user=self.request.user,
                cloth_id = self.kwargs['pk']
            )
            if is_favourites:
                context['is_favourites'] = True
        except Favourites.DoesNotExist:
            context['is_favourites'] = False
        return context


def add_to_favorites(request, pk):
    """
    Добавить в избранное
    """
    favourites = Favourites.objects.create(
        user = request.user,
        cloth_id = pk
    )
    favourites.save()
    return redirect('cloth:detail', pk=pk)

def delete_from_favorites(request, pk):
    """
    Удалить из избранного
    """
    favourites = Favourites.objects.get(
        user = request.user,
        cloth_id = pk
    )
    favourites.delete()
    return redirect('cloth:detail', pk=pk)

class ClothListView(ListView):
    model = Cloth
    template_name = "pages/cloth/list.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['object_list'] = News.objects.all().order_by('-id')
    #     return context

class UserFavouritesListView(ListView):
    model = Favourites
    template_name = "pages/cloth/favourites.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Favourites.objects.filter(user=self.request.user).order_by('-date_created')
        return context
