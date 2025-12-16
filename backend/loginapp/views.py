from django.http import JsonResponse
from django.shortcuts import render

def login_view(request):
    return render(request, "login.html")  # o lo que necesites

def api_login(request):
    return JsonResponse({"message": "API login OK"})
