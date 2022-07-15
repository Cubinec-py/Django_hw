from django import forms

from triangle.models import Person


class TriangleForm(forms.Form):
    catet1 = forms.IntegerField(label='Катет №1', min_value=1, required=True)
    catet2 = forms.IntegerField(label='Катет №2', min_value=1, required=True)


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'email']
