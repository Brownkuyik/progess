from django import forms
from .models import comment


class commentform(forms.Modelform):
    name = forms.CharField(max_length=100, label='NAME', widget=forms.TextInput(attrs={'placeholder':'Your Name', 'class' :'form-control'}))
    subject = forms.CharField(max_length=200, label='SUBJECT', widget=forms.TextInput(attrs={'placeholder':'subject', 'class' :'form-control'}))
    phone = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Your Phone', 'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Your Email', 'class':'form-control'}))
    image = forms.ImageField()
    text = forms.Textarea(attrs={'placeholder':'text', 'class':'form-control'})

    class meta:
        model = comment
        fields = '__all__'