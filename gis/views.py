from django.http import HttpResponse
import datetime
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import AnonymousUser
from django.shortcuts import redirect
from accounts.models import Profile, Address
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

    return render(request, 'home.html', data)

def facebook(request):
    return render(request, 'facebook.html')

def demo(request):
    return render(request, 'demo.html')

def profile_form(request):
    profile = Profile.objects.get(owner=request.user)
    profile.address.raw = request.POST.get('address')
    profile.address.save()
    return redirect('home')

