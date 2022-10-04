from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.contrib.auth import authenticate,login,logout
# from django.contrib.messages import constants as messages
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from auth_app.models import UserProfile


# login view
def signin(request):
    if request.method == 'GET':
        context = {}
        if request.user.is_authenticated:
            return redirect('dashboard')
        else:
            return render(request,'auth_screens/login.html')

    if request.method == 'POST':
        email = request.POST.get('email')
        password =request.POST.get('password')
        user = authenticate(request,username=email,password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            context = {}
            context['error_msg'] = 'Invalid Username or Password'
            return render(request,'auth_screens/login.html',context)

        # return render(request,'auth_screens/login.html')

# logout view
def logout_view(request):
    logout(request)
    return redirect('/')