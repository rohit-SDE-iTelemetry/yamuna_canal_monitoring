from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.


# login page
def login(request):
    if request.method == 'GET':
        context = {}
        return render(request,'')
