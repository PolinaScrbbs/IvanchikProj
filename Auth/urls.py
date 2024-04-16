from django.contrib import admin
from django.urls import path

from .views import login, clear_session

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', clear_session, name='logout')
]
