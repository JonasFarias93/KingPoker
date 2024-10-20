from django.shortcuts import render, redirect, get_object_or_404
from players.models import Participant



def players_views(request):
    players = Participant.objects.all()
    search = request.GET.get('search')
    if search:
        players = players.filter(name__icontains = search)
    return render(request,'players.html',
    {'players': players})

def index_views(request):
    return render(request, 'login.html')
