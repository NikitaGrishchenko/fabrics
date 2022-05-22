from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView, ListView, TemplateView
from django.views.generic.detail import DetailView

# from .filters import ClothFilter, SupplierFilter
from .forms import ClothShowroomForm
from .models import ClothShowroom


class ClothShowroomView(FormView):
    """
    Регистрация пользовател
    """

    template_name = "pages/showroom/add.html"
    form_class = ClothShowroomForm
    success_url = reverse_lazy("showroom:confirmation")

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/')
        return super(ClothShowroomView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        cloth = form.save(commit=False)
        cloth.user = self.request.user
        cloth.save()
        form.save_m2m()
        return super().form_valid(form)


class ClothShowroomListView(ListView):

    model = ClothShowroom
    template_name = "pages/showroom/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = ClothShowroom.objects.filter(is_confirmed=True).order_by('-id')

        return context


class ConfirmationShowroom(TemplateView):
    """
    Подтверждение шоурум
    """

    template_name = "notice/confirmation-showroom.html"


