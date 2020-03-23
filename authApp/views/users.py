from django.contrib.auth import authenticate, login
from django.forms import modelformset_factory
from django.shortcuts import render
from django.views import View
from django.conf import settings
from authApp.models import User

from authApp.forms import UserGroupForm, MyFormSet


class UsersView(View):
    template_name = r"authApp\users.html"
    user_formset = modelformset_factory(
        User,
        fields={'username', 'email'},
        form=UserGroupForm,
        extra=1,
        formset=MyFormSet,
    )
    formset = user_formset()

    def get(self, request):
        context = {
            "formset": self.formset,
            'extended_template': settings.BASE_WITH_HEADER_TEMPLATE,
        }
        return render(request, self.template_name, context)
