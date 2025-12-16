from django.urls import path
from .views import login_view, api_login

urlpatterns = [
    path('login/', login_view),
    path('api/login/', api_login),
]
