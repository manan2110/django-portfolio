from django.shortcuts import render
from .models import *
# Create your views here.


def index(request):
    profile = Profile.objects.get(id=1)
    dp = DP.objects.get(id=1)
    projects = Project.objects.all()
    return render(request, 'index.html', {'profile': profile, 'dp': dp, 'projects': projects})
