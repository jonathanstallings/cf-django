from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic

from .models import User


def IndexView(request):
    context = {'user_list': User.objects.order_by('first_name')}
    return render(request, 'users/index.html', context)


def DetailView(request, user_id=None):
    context = {'user': get_object_or_404(User, pk=user_id)}
    return render(request, 'users/detail.html', context)


def AddView(request):
    user = {
        'id': 0,
        'first_name': "",
        'last_name': "",
        'email': ""
    }
    context = {
        'user': user
    }

    return render(request, 'users/detail.html', context)
