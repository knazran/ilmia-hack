from django import forms

# Form styling
# replace this with your CSS classes later
css_class = "form-control appearance-none w-full bg-gray-200 border border-gray-200 text-black rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
nec1_course =['Social Sciences, Business and Law', 'Health and Welfare',
       'Engineering, Manufacturing and Construction',
       'Sciences, Mathematics and Computing', 'Education',
       'Arts and Humanities', 'Services', 'Agriculture and Veterinary',
       'General Programmes']
states = ['Wilayah Persekutuan Kuala Lumpur', 'Sabah',
       'Wilayah Persekutuan Labuan', 'Selangor', 'Sarawak', 'Kelantan',
       'Johor', 'Perak', 'Terengganu', 'Kedah', 'Pulau Pinang',
       'Negeri Sembilan', 'Luar Negara', 'Melaka', 'Pahang',
       'Wilayah Persekutuan Putrajaya', 'Perlis']

class SurveyFormStepOne(forms.Form):
    course_of_study = forms.ChoiceField(label=False, widget=forms.Select(
        attrs={'class': css_class }))
    # course_of_study = forms.CharField(max_length=100)

    def __init__(self, *args, **kwargs):
        super(SurveyFormStepOne, self).__init__(*args, **kwargs)
        self.fields['course_of_study'].choices = [
            ('Computer Science', 'Computer Science'), ('Economics', 'Economics')]
        nec1 = [(item, item) for item in nec1_course]
        self.fields['course_of_study'].choices = self.fields['course_of_study'].choices + nec1


class SurveyFormStepTwo(forms.Form):
    # university = forms.CharField(max_length=100)
    university = forms.ChoiceField(label=False, widget=forms.Select(
        attrs={'class': css_class }))

    def __init__(self, *args, **kwargs):
        super(SurveyFormStepTwo, self).__init__(*args, **kwargs)
        self.fields['university'].choices = [
            ('UIA', 'UIA'), ('UiTM', 'UiTM')]


class SurveyFormStepThree(forms.Form):
    # current_location = forms.CharField(max_length=100)
    current_location = forms.ChoiceField(label=False, widget=forms.Select(
        attrs={'class': css_class }))

    def __init__(self, *args, **kwargs):
        super(SurveyFormStepThree, self).__init__(*args, **kwargs)
        self.fields['current_location'].choices = [(item, item) for item in states]
