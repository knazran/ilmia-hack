from django.shortcuts import render

def home(request):
    context = {}
    template = 'home.html'
    return render(request, template, context)

def survey(request):
    context = {}
    template = 'survey.html'
    return render(request, template, context)

def results(request):
    context = {}
    template = 'results.html'
    return render(request, template, context)
