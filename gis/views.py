from django.http import HttpResponse
import datetime
from django.shortcuts import get_object_or_404, render

def home(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return render(request, 'home.html')

def facebook(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return render(request, 'facebook.html')

