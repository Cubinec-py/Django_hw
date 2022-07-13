from django import forms


class TriangleForm(forms.Form):
    catet1 = forms.IntegerField(label='Катет №1', min_value=1, required=True)
    catet2 = forms.IntegerField(label='Катет №2', min_value=1, required=True)
