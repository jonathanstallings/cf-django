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


def about(request):
    return render(request, 'users/about.html', context=None,)


def edit(request, user_id):
    if user_id != '0':
        u = get_object_or_404(User, pk=user_id)
    else:
        u = User()

    u.first_name = request.POST['first_name']
    u.last_name = request.POST['last_name']
    u.email = request.POST['email']
    u.notes = request.POST['notes']

    u.save()
    return HttpResponseRedirect(reverse('users:index'))


def delete(request, user_id):
    u = get_object_or_404(User, pk=user_id)
    u.delete()
    return HttpResponseRedirect(reverse('users:index'))
