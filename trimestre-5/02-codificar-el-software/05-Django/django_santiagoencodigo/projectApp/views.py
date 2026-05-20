from django.shortcuts import HttpResponse

def index(Request):
    return HttpResponse("My first App | santiagoencodigo")

# Create your views here.