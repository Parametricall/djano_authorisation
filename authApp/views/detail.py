from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User as DjangoUser
from django.conf import settings

from authApp.forms import UserForm


class DetailView(View):
    template_name = "authApp\profile.html"

    def get(self, request, person_id=1):

        user = DjangoUser.objects.get(pk=person_id)

        form = UserForm(instance=user)
        context = {
            'form': form,
            'person_id': person_id,
        }
        return render(request, self.template_name, context)
