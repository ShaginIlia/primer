from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister
from .models import *


def platform(request):
    return render(request, 'platform.html')


def games(request):
    game = Game.objects.all()
    context = {
        'game': game
    }
    return render(request, 'games.html', context)


def cart(request):
    return render(request, 'cart.html')


def sign_up_by_django(request):
    info = {}
    errors = []
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = int(form.cleaned_data['age'])

            existing_users = Buyer.objects.all().values_list('name', flat=True)

            if password == repeat_password and age >= 18 and username not in existing_users:
                new_user = Buyer.objects.create(name=username, age=age)
                return HttpResponse(f'Приветствуем, {new_user.name}!')
            elif password != repeat_password:
                errors.append('Пароли не совпадают')
                return HttpResponse(f'Пароли не совпадают')
            elif age < 18:
                errors.append('Вы должны быть старше 18')
                return HttpResponse(f'Вы должны быть старше 18')
            elif username in existing_users:
                errors.append('Пользователь уже существует')
                return HttpResponse(f'Пользователь уже существует')
    else:
        form = UserRegister()
    info['error'] = errors
    return render(request, 'registration_page.html', {'form': form, 'info': info})

