from django.shortcuts import render

def players_views(request):
    return render(request,'players.html',
    {'Participant':{'name':'Jonas'}

    })

def index_views(request):
    return render(request, 'index.html')