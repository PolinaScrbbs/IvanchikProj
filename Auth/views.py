from django.shortcuts import render, redirect
from .forms import LoginForm
from rest_framework import status
import requests
from django.http import HttpResponse, HttpResponseRedirect

def login(request):
    form = LoginForm(request.POST or None)
    next_url = request.GET.get('next')
    print(next_url)

    if request.method == 'POST' and form.is_valid():
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')

        api_url = 'http://127.0.0.1:8000/auth/login/'
        response = requests.post(api_url, data={'email': email, 'password': password})

        if response.status_code == 200:
            token = response.json().get('token')
            request.session['token'] = token
            
            # Если есть параметр next, выполняем перенаправление на него
            if next_url:
                return redirect(next_url)
            else:
                return redirect('index')

        else:
            return render(request, 'login.html', {'form': form})

    return render(request, 'login.html', {'form': form})

def clear_session(request):
    request.session.clear()
    # Получаем предыдущий URL, если он есть, и перенаправляем пользователя на него
    previous_url = request.META.get('HTTP_REFERER')
    if previous_url:
        return HttpResponseRedirect(previous_url)
    else:
        # Если предыдущего URL нет, перенаправляем на главную страницу или другую страницу по умолчанию
        return HttpResponseRedirect('/')



