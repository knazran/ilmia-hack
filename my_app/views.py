from django.shortcuts import render
from my_app.forms import SurveyFormStepOne, SurveyFormStepTwo
from formtools.wizard.views import SessionWizardView

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

def skillgap(request):
    context = {}
    template = 'skillgap.html'
    return render(request, template, context)

def mentors(request):
    context = {}
    template = 'mentors.html'
    return render(request, template, context)

class FormWizardView(SessionWizardView):
    template_name = "survey.html"
    form_list = [SurveyFormStepOne, SurveyFormStepTwo]
    def done(self, form_list, **kwargs):
        return render(self.request, 'results.html', {
            'form_data': [form.cleaned_data for form in form_list],
        })