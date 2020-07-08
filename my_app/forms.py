from django import forms

class SurveyFormStepOne(forms.Form):
    course_of_study = forms.CharField(max_length=100)
class SurveyFormStepTwo(forms.Form):
    university = forms.CharField(max_length=100)
class SurveyFormStepThree(forms.Form):
    current_location = forms.CharField(max_length=100)