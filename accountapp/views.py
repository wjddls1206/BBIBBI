from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView


# Create your views here.
class TestView(TemplateView):
    template_name = 'accountapp/test.html'

class LogInView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'accountapp/login.html'