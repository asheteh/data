from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # order by used to show most recent home 1st
   
    return render(request,"index.html")
