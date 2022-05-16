from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .filters import ClothFilter
from .forms import FeedbackToClothForm
from .models import Cloth, Favourites, FeedbackToCloth, Supplier


class ClothDetailView(DetailView):
    model = Cloth
    template_name = "pages/cloth/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = Cloth.objects.get(id=self.kwargs['pk'])
        if self.request.user.is_authenticated:
            try:

                is_favourites = Favourites.objects.get(
                    user=self.request.user,
                    cloth_id = self.kwargs['pk']
                )
                if is_favourites:
                    context['is_favourites'] = True
            except Favourites.DoesNotExist:
                context['is_favourites'] = False
        else:
            context['is_favourites'] = False

        context['feedbacks'] = FeedbackToCloth.objects.filter(cloth_id=self.kwargs['pk']).order_by('-date_created')

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ClothFilter(self.request.GET, queryset=self.get_queryset())
        return context

class UserFavouritesListView(ListView):
    model = Favourites
    template_name = "pages/cloth/favourites.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Favourites.objects.filter(user=self.request.user).order_by('-date_created')
        return context


def send_feedback(request, pk):
    """
    Отправка отзыва
    """
    if request.method == 'POST':
        form = FeedbackToClothForm(request.POST)
        if form.is_valid():

            try:
                cloth = Cloth.objects.get(id=pk)
            except Cloth.DoesNotExist:
                return redirect('user:error')

            feedback_to_cloth = FeedbackToCloth(
                user=request.user,
                cloth=cloth,
                rating=form.cleaned_data['rating'],
                text=form.cleaned_data['text'],
            )
            feedback_to_cloth.save()
        return redirect('cloth:detail', pk=pk)



class SupplierListView(ListView):
    """
    Лист поставщиков
    """
    model = Supplier
    template_name = "pages/supplier/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Supplier.objects.all().order_by('-id')
        return context


class SupplierDetailView(DetailView):
    model = Supplier
    template_name = "pages/supplier/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = Supplier.objects.get(id=self.kwargs['pk'])
        context['cloths'] = Cloth.objects.filter(supplier_id=self.kwargs['pk'])

        return context
