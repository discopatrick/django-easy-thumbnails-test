from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Person

class PersonList(ListView):
    model = Person

class PersonDetail(DetailView):
    model = Person
