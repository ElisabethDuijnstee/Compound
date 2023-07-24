from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# view function takes a request and gives a response
# request handler (called action in django)

def say_hello(request):
    x = 1
    y = 2
    return render(request, 'hello.html',{'name':'Elisabeth'})
    
