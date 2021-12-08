from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import View
from .models import CustomUser, FirstOrder
from django.conf import settings
from .forms import ContactUsForm, FormOrderOne, FormOrderTwo
from django.views.generic import (
    CreateView,
    DetailView,
    TemplateView
)


def home(request):
    return render(request, 'front/home.html')


class SignUpForm(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'account/signup.html'

    def form_valid(self, form):
        form.instance.client = self.request.user
        return super().form_valid(form)


class ContactUsFormView(View):
    def get(self, *args, **kwargs):
        form = ContactUsForm()
        context = {
            'form': form
        }
        return render(self.request, 'front/home.html', context)

    def post(self, *args, **kwargs):
        form = ContactUsForm(self.request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            messages.warning(self.request, "Your message was sent successfully")
            print('This form is valid')
            return redirect('home')
        return render(self.request, 'front/home.html', {'form': form})


class ViewFormOrder(FormView):
    template_name = 'front/order1.html'
    form_class = FormOrderOne
    success_url = 'commit'

    def form_valid(self, form):
        return super().form_valid(form)


class ViewFormOrder2(FormView):
    template_name = 'front/order2.html'
    form_class = FormOrderTwo
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        return super().form_valid(form)

