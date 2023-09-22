from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_hello(request):
    # return HttpResponse("Hello world")
    return render(request, 'home.html', {'name': "sundar"})

# def user(request):
#     data = request.POST.get('name')
#     return render(request, 'home.html', {'name': data})