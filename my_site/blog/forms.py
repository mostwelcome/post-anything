from django import forms


class PostForms(forms.Form):
    image = forms.FileField()
    text = forms.CharField(label="Description")
