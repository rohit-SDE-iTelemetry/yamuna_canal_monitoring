from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from auth_app.models import UserProfile


# login page
def login(request):
    if request.method == 'GET':
        context = {}
        return render(request,'auth_screens/login.html')

    if request.method == 'POST':
        return render(request,'auth_screens/login.html')


