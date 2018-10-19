from django.shortcuts import render
from .models import Picture


def index(request):
    set=Picture.objects.all()
    context={
        "objects":set,
        
    }
    return render(request,"img/index.html",context)
