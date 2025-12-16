from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("Backend OK (login en /login/)")

urlpatterns = [
    path('', home),  # GET /
    path('admin/', admin.site.urls),
    path('', include('loginapp.urls')),  # enruta /login/ a tu app
]
