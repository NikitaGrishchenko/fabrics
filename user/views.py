
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView, TemplateView
from django.views.generic.detail import DetailView

from .forms import UserRegistrationForm

# from .models import MeterReadings, QuestionsFromGuests

User = get_user_model()



class AccountVeiw(TemplateView):

    template_name = "pages/account.html"

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/')
        return super(AccountVeiw, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_user = self.request.user
        context['user'] = User.objects.get(id=current_user.id)
        return context


class RegistrationView(FormView):
    """
    Регистрация пользовател
    """

    template_name = "pages/registration.html"
    form_class = UserRegistrationForm
    success_url = reverse_lazy("user:thanks")

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return super(RegistrationView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save(commit=False)
        user.open_password = form.cleaned_data["password"]
        user.username = user.email
        user.set_password(form.cleaned_data["password"])
        user.save()
        form.save_m2m()
        return super().form_valid(form)


class ThanksView(TemplateView):
    """
    Страница благодарности
    """

    template_name = "notice/thanks.html"

class SuccessView(TemplateView):
    """
    Страница успешного выполненного действия
    """

    template_name = "notice/success.html"

class ErrorView(TemplateView):
    """
    Страница ошибки
    """

    template_name = "notice/error.html"
