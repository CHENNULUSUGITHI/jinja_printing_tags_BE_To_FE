from django.shortcuts import render

# Create your views here.
def wish(request):
    d={'name':'AMMA','age':40}
    return render(request,'wish.html',context=d)