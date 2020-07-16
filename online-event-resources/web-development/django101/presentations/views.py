from django.shortcuts import render, HttpResponse
from django.views import generic

from .models import Presentation

# Create your views here.

class IndexView(generic.ListView):
    # Object name in the template
    context_object_name = 'presentations'

    # Data to display
    def get_queryset(self):
        return Presentation.objects.all()