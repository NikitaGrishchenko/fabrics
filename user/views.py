
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView, TemplateView
from django.views.generic.detail import DetailView

# from .forms import (CallingWizardForm, MeterReadingsForm,
#                     QuestionsFromGuestsForm, QuestionsUserForm,
#                     UserRegistrationForm)
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
