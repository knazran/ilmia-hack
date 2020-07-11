from django.shortcuts import render
from my_app.forms import SurveyFormStepOne, SurveyFormStepTwo, SurveyFormStepThree
from formtools.wizard.views import SessionWizardView
import pandas as pd
import json

# Global context to read data into pandas
df_tracer = pd.read_csv('my_app/static/data/7_tracer_study.csv')


def home(request):
    context = {}
    template = 'home.html'
    return render(request, template, context)


def survey(request):
    context = {
        'form1': SurveyFormStepOne,
        'form2': SurveyFormStepTwo,
        'form3': SurveyFormStepThree
    }
    template = 'survey.html'
    return render(request, template, context)

# data = {
#     datasets: [{
#         data: [10, 20, 30]
#     }],

#     // These labels appear in the legend and in the tooltips when hovering different arcs
#     labels: [
#         'Red',
#         'Yellow',
#         'Blue'
#     ]
# };
def results(request):
    # json_data = json.loads(request.body)
    form = SurveyFormStepOne(request.POST)  # A form bound to the POST data
    if form.is_valid():
        print(form.cleaned_data['course_of_study'])
        course = form.cleaned_data['course_of_study']

        df_fresh_grad = df_tracer.query("nec1_desc=='{}' & age < 25".format(course))

        salary_data = df_fresh_grad['monthly_income']\
            .value_counts(1).round(3)
        salary_chart_payload = {
            'datasets': [{
                'data': list(salary_data.values * 100)
            }],
            'labels': list(salary_data.keys())
        }
        top_5_industries_labels = list(df_fresh_grad['msic1'].value_counts(1)[:5].keys())
        top_5_industries_values = list(df_fresh_grad['msic1'].value_counts(1).round(3)[:5].values * 100)
        
    context = {
        "course": course,
        "average_salary": 3000,
        "salary_chart_payload": salary_chart_payload,
        "top_5_industries_labels": top_5_industries_labels,
        "top_5_industries_values": top_5_industries_values,
        # "university": json_data["university"],
        # "location": json_data["location"],
    }
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
