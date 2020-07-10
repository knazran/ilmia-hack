from django.shortcuts import render
from my_app.forms import SurveyFormStepOne, SurveyFormStepTwo, SurveyFormStepThree
from formtools.wizard.views import SessionWizardView
import pandas as pd

# Global context to read data into pandas
# df_tracer = pd.read_csv('my_app/static/data/2_job_vacancy.csv')

def home(request):
    context = {}
    template = 'home.html'
    return render(request, template, context)

def survey(request):
    context = {
        'form1' : SurveyFormStepOne,
        'form2' : SurveyFormStepTwo,
        'form3' : SurveyFormStepThree
    }
    template = 'survey.html'
    return render(request, template, context)

def results(request):
    print(request.body)
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

def submitFormEndpoint(request):
    # Do something
    template = 'results.html'
    return render(request, template, context) 

class FormWizardView(SessionWizardView):
    template_name = "survey.html"
    form_list = [SurveyFormStepOne, SurveyFormStepTwo, SurveyFormStepThree]
    def done(self, form_list, **kwargs):
        return render(self.request, 'results.html', {
            'form_data': [form.cleaned_data for form in form_list],
        })