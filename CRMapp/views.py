from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from .forms import UserProfileForm
from .models import *
# Create your views here.

def webUser(request):
    if request.method == 'POST':
        form= UserProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('accounts/registered')
    else:
        user=request.user
        profile=user.profile
        form = UserProfileForm(instance=profile)