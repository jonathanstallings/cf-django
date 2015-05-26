from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import User

# Create your views here.

def IndexView(generic.ListView):
    template_name = 'users/index.html'
    context_object_name = 'lat'
