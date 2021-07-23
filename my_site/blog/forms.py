from django import forms


class PostForms(forms.Form):
    text = forms.CharField()
    image = forms.FileField()
