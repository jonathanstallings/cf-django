from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic

from .models import User

# Create your views here.

def IndexView(request):
    return HttpResponse("Hello World")
