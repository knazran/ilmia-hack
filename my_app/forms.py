from django import forms

# Form styling
# replace this with your CSS classes later
css_class = "form-control appearance-none w-full bg-gray-200 border border-gray-200 text-black rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500"


class SurveyFormStepOne(forms.Form):
    course_of_study = forms.ChoiceField(label="Course of Study", widget=forms.Select(
        attrs={'class': css_class }))
    # course_of_study = forms.CharField(max_length=100)

    def __init__(self, *args, **kwargs):
        super(SurveyFormStepOne, self).__init__(*args, **kwargs)
        self.fields['course_of_study'].choices = [
            ('Computer Science', 'Computer Science'), ('Economics', 'Economics')]


class SurveyFormStepTwo(forms.Form):
    # university = forms.CharField(max_length=100)
    university = forms.ChoiceField(label="University", widget=forms.Select(
        attrs={'class': css_class }))

    def __init__(self, *args, **kwargs):
        super(SurveyFormStepTwo, self).__init__(*args, **kwargs)
        self.fields['university'].choices = [
            ('UIA', 'UIA'), ('UiTM', 'UiTM')]


class SurveyFormStepThree(forms.Form):
    # current_location = forms.CharField(max_length=100)
    current_location = forms.ChoiceField(label="Current Location", widget=forms.Select(
        attrs={'class': css_class }))

    def __init__(self, *args, **kwargs):
        super(SurveyFormStepThree, self).__init__(*args, **kwargs)
        self.fields['current_location'].choices = [
            ('Kuala Lumpur', 'Kuala Lumpur'), ('Kelantan', 'Kelantan')]
