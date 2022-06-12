from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

def index(request):
    return redirect('/time')


def index1(request):
    context = {
        "date": strftime("%Y-%m-%d ", gmtime()),
        "time": strftime("%H:%M %p",gmtime())

    }
    return render(request,'index.html', context)