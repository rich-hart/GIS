from django.http import HttpResponse
import datetime
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import AnonymousUser
from django.shortcuts import redirect
from accounts.models import Profile, Address
from django.conf import settings

def home(request):
    user = request.user
#    import ipdb; ipdb.set_trace()
    if user.is_anonymous:
        data = {
            'username': None
        }
    elif user.is_superuser:
        data = {
            'username': user.username
        }
    else:
        data = {
            'username': user.username,
            'address': user.profile.address.raw,
        }
    data.update({'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY})
    return render(request, 'home.html', data)

def facebook(request):
    return render(request, 'facebook.html')

def demo(request):
    user = request.user
#    import ipdb; ipdb.set_trace()
    if user.is_anonymous:
        data = {
            'username': None
        }
    elif user.is_superuser:
        data = {
            'username': user.username
        }
    else:
        data = {
            'username': user.username,
            'address': user.profile.address.raw,
        }

    return render(request, 'demo.html', data)

def profile_form(request):
#    import ipdb; ipdb.set_trace()
    profile = Profile.objects.get(owner=request.user)
    profile.address.raw = request.POST.get('address')
    profile.address.save()
    return redirect('home')

