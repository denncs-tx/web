from django.shortcuts import render

from django.views.generic import ListView


# Create your views here.
class IndexView(ListView):
    template_name = 'assets/index.html'

    def get_queryset(self):
        return None
