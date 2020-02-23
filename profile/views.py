from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views import View
from django.conf import settings

from .models import Profile

@login_required(login_url='/admin/login/')
def index(request):
    context = {
        'MAPS_API_KEY' : settings.MAPS_API_KEY
    }
    return render(request, 'userprofile/index.html', context)