from django.http import HttpResponse
import datetime
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import AnonymousUser
from django.shortcuts import redirect
from accounts.models import Profile #,Address
from django.conf import settings


def raffle(request):
    return render(request, 'raffle.html')

def qr_code_validator(request,key):
#    import ipdb; ipdb.set_trace()
     
    return redirect('/?tribble={}#profile'.format(key))
def home(request):
    data = {
      'username': None,
      'address': None,
      'tribble': None,
      'google_id': None,
      'longitude': None,
      'latitude': None,
      'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY,
    }
#    import ipdb; ipdb.set_trace()
    user = request.user
#    import ipdb; ipdb.set_trace()

    if user.is_anonymous:
        pass
    elif user.is_superuser:
        data['username'] = user.username
    else:
        data['username'] = user.username
#        data['address'] = user.profile.address.raw
#        data['google_id'] = user.profile.address.google_id
#        data['longitude'] = user.profile.address.longitude
#        data['latitude'] = user.profile.address.latitude
        data['tribble']= request.GET.get('tribble')
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
    profile.address.google_id = request.POST.get('google_id')
    profile.address.longitude = request.POST.get('longitude')
    profile.address.latitude = request.POST.get('latitude')
    profile.address.save()
    return redirect('/#profile')

def lcars(request):
    return render(request, 'LCARS-SDK_16323.311/interfaces/color-generator/index.html')

