from django.shortcuts import render
from virtusa import models

# Create your views here.
def modelsview(request):
    k = models.Ml_models.objects.all()
    mlist = [{'name':i.name,'image':i.image,'summary':i.summary } for i in k]
    return render(request,'models.html',{'models':mlist})
# 
# def modelsresult(request,item_url):
#     return render(request,'models.html',{'models':mlist})
