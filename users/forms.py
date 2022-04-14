from django import forms

class ContactUsForm(forms.Form):
    name = forms.CharField(label='Name', max_length=64)
    email = forms.EmailField(label='Email')
    message = forms.CharField(widget=forms.Textarea(attrs={"rows":10, "cols":30}))