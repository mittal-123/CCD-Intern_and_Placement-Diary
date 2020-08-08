from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

from django.contrib.auth.mixins import LoginRequiredMixin
from . import models

# Create your views here.

class CompanyListView(LoginRequiredMixin, ListView):
    model = models.Company
    fields = ('name', 'POC', 'CPOC', 'additional_POC', 'email', 'logo', 'placement', 'internship')
    template_name = 'diary/company_list.html'

class CompanyCreateView(LoginRequiredMixin, CreateView):
    model = models.Company
    fields = ('name', 'POC', 'CPOC', 'additional_POC', 'email', 'logo', 'placement', 'internship')
    template_name = 'diary/company_create.html'
