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
        'form1' : SurveyFormStepOne,
        'form2' : SurveyFormStepTwo,
        'form3' : SurveyFormStepThree
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
    form1 = SurveyFormStepOne(request.POST)  # A form bound to the POST data
    form3 = SurveyFormStepThree(request.POST)
    if form1.is_valid() and form3.is_valid():
        course = form1.cleaned_data['course_of_study']
        location = form3.cleaned_data['current_location']
        
        if course == 'Computer Science':
            df_fresh_grad = df_tracer.query("nec3_desc=='Computer science' & age < 25 & working_state=='{}'".format(location))
            print('Computer sc')
        elif course == 'Economics':
            df_fresh_grad = df_tracer.query("nec2_desc=='Economics' & age < 25 & working_state=='{}'".format(location))
        else:
            df_fresh_grad = df_tracer.query("nec1_desc=='{}' & age < 25 & working_state=='{}'".format(course, location))
            print('asdasda sc')

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

        time_to_get_work = (df_fresh_grad['time_to_obtain_work'].value_counts(1) * 100 )[[0]].to_dict()
        salary_range = (df_fresh_grad['monthly_income'].value_counts(1)*100)[[0]].to_dict()
        
    context = {
        "course": course,
        "average_salary": 3000,
        "salary_chart_payload": salary_chart_payload,
        "salary_range": salary_range,
        "top_5_industries_labels": top_5_industries_labels,
        "top_5_industries_values": top_5_industries_values,
        "location": location,
        "time_to_get_work": time_to_get_work
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
