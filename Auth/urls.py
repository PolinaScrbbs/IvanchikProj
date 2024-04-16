from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView

from .views import UsersView, LoginView

#Auth
urlpatterns = [
    path('signup/', UsersView.as_view(), name='auth-signup'),
    path('login/', LoginView.as_view(), name='auth-login'),
    path('token-refresh/', TokenRefreshView.as_view)
]