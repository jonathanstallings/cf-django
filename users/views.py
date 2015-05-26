from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import User


def index(request):
    context = {'user_list': User.objects.order_by('first_name')}
    return render(request, 'users/index.html', context)


def detail(request, user_id=None):
    context = {'user': get_object_or_404(User, pk=user_id)}
    return render(request, 'users/detail.html', context)


def add(request):
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
        user = get_object_or_404(User, pk=user_id)
    else:
        user = User()

    user.first_name = request.POST['first_name']
    user.last_name = request.POST['last_name']
    user.email = request.POST['email']
    user.notes = request.POST['notes']

    if not user.protected:  # Prevent modificaton of special users.
        user.save()
    return HttpResponseRedirect(reverse('index'))


def delete(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if not user.protected:  # Prevent deletion of special users.
        user.delete()
    return HttpResponseRedirect(reverse('index'))
