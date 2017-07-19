from .models import Profile

def save_profile(backend, user, response, *args, **kwargs):
    (profile, created) = Profile.objects.get_or_create(owner=user)
    profile.save()
