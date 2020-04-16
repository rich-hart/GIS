from .models import Player

def create_player(backend, user, response, *args, **kwargs):
    (player, created) = Player.objects.get_or_create(user=user)
    player.save()
