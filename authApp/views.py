from django.contrib import messages
# from django.contrib.auth.forms import l
from django.contrib.auth.models import User
from django.db import transaction
from django.forms import formset_factory, modelformset_factory
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User as DjangoUser
from django.urls import reverse

from authApp.forms import UserForm
from authApp.models import Profile
from authApp.forms import *
# from auth.models import User

# Create your views here.
def index(request):
    return render(request, r'authApp\base.html', {'person_id': 1})


def detail(request, person_id):

    user = DjangoUser.objects.get(pk=person_id)

    form = UserForm(instance=user)

    if request.method == 'POST':
        form = UserForm(request, instance=user)

    return render(request, 'authApp\profile.html', {'form': form, 'person_id': person_id})

def create_user_view(request):

    form = CreateUserForm()

    if request.method == 'POST':
        if request.POST['create_user'] == 'Create User':
            form = CreateUserForm(request.POST)

            if form.is_valid():
                form.save()
                user = User.objects.get(username=form.cleaned_data['username'])
                user.set_password(form.cleaned_data['password'])
                user.save()


        return HttpResponseRedirect(reverse('auth:index'))


    context = {
        'form': form,
    }

    return render(request, 'authApp\create.html', context)

def user_formset_view(request):

    user_formset = modelformset_factory(
        User,
        fields={'username', 'email'},
        form=UserGroupForm,
        extra=0,
        formset=MyFormSet,
    )
    formset = user_formset()

    if request.method == 'POST':
        formset = user_formset(request.POST, request.user)
        if request.POST.get('username'):
            username = request.POST.get('username')
            user = User.objects.get(username=username)
            return HttpResponseRedirect(reverse('auth:profile', kwargs={'person_id': user.id}))

    context = {
        'formset': formset,
    }

    return render(request, 'authApp\users.html', context)



