from django.shortcuts import render
from django.contrib.auth.decorators import login_required


#########################################################################################################
# MASTER MODULE
#########################################################################################################
# add station category view
@login_required(login_url='/')
def master(request):
    if request.method == 'GET':
        context = {}
        return render(request,'master/master-view.html',context)

# add station category view
@login_required(login_url='/')
def add_category(request):
    if request.method == 'GET':
        context = {}
        return render(request,'master/add-category.html',context)

# add params view
@login_required(login_url='/')
def add_param(request):
    if request.method == 'GET':
        context = {}
        return render(request,'master/add-params.html',context)
