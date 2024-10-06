from django.shortcuts import render
from players.models import Participant

def players_views(request):
    players = Participant.objects.all()
    return render(request,'players.html',
    {'players': players}
    )

def index_views(request):
    return render(request, 'index.html')

