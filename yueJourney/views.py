from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def aboutMe(request):
    return render(request, 'aboutme.html')
