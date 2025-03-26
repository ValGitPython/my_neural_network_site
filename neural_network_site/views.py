from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def applications(request):
    return render(request, 'applications.html')

def prompts(request):
    return render(request, 'prompts.html')

def future(request):
    return render(request, 'future.html')
