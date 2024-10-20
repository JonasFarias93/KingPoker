from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

def index_views(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('players_list')  # Redirecionar para a página dos jogadores ou outra
        else:
            # Tratar erro de login
            error_message = "Credenciais inválidas."
            return render(request, 'accounts/login.html', {'error_message': error_message})

    return render(request, 'accounts/login.html', {'is_register': False})  # Exibir o login por padrão


def register_view(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            # Opcional: fazer login após registro
            username = user_form.cleaned_data.get('username')
            raw_password = user_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('players_list')  # Redirecionar após o registro

    else:
        user_form = UserCreationForm()
    
    return render(request, 'accounts/login.html', {'user_form': user_form, 'is_register': True})
