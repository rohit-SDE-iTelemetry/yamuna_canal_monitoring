from django.shortcuts import render
from django.contrib.auth.decorators import login_required


#########################################################################################################
# REPORT MODULE
#########################################################################################################
@login_required(login_url='/')
def report(request):
    if request.method == 'GET':
        context = {}
        return render(request,'reports/report.html',context)