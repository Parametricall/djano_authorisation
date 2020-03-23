from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.views import View
from django.conf import settings


class IndexView(View):
    template_name = settings.BASE_WITH_HEADER_TEMPLATE

    def get(self, request):
        context = {}
        if request.user == 'admin':
            context['user'] = request.user
        return render(request, self.template_name, context)

    def post(self, request):
        context = {}
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            context['user'] = user
        return render(request, self.template_name, context)
