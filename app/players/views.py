from django.shortcuts import render

def players_views(request):
    return render(request,'players.html')

def index_views(request):
    return render(request, 'index.html')