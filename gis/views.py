from django.http import HttpResponse
import datetime
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import AnonymousUser
def home(request):
    import ipdb; ipdb.set_trace()
    if request.user.is_anonymous:
        data = {
            'username': None
        }
    else:
        data = {
            'username': request.user.username
        }

    return render(request, 'home.html', data)

def facebook(request):
    return render(request, 'facebook.html')

def demo(request):
    return render(request, 'demo.html')

