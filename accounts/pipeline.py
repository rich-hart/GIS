from .models import Profile
#from .models import Address
def save_profile(backend, user, response, *args, **kwargs):
    (profile, created) = Profile.objects.get_or_create(owner=user)
#    if not profile.address:
#        address = Address()
#        address.save()
#        profile.address = address
    profile.save()
