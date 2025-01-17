from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.shortcuts import redirect, render


def create(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('flashcards:create')
        return render(request, 'create_user.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm')

        user = User.objects.filter(username=username)
        if user.exists():
            messages.add_message(
                request,
                constants.ERROR,
                'Este nome de usuário já existe.',
            )
            return redirect('users:create')
        if password != confirm:
            messages.add_message(
                request,
                constants.ERROR,
                'As senhas não coinciedem.',
            )
            print('as senhas não são iguais...')
            return redirect('users:create')
        try:
            user = User.objects.create_user(
                username=username,
                password=confirm,
            )
            return redirect('users:login')
        except Exception:
            return redirect('users:create')


def signin(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/flashcards/new_flashcard')
        return render(request, 'login_user.html')

    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(request, username=username, password=password)
        if user:
            messages.add_message(
                request, constants.SUCCESS, 'Usuário logado com sucesso!'
            )
            auth.login(request, user)
            return redirect('flashcards:home')

        messages.add_message(
            request,
            constants.ERROR,
            'Nome de usuário ou senha inválidos.',
        )
        return redirect('users:login')


def logout(request):
    auth.logout(request)
    return redirect('users:login')
