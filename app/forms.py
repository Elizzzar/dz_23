from django import forms
from .models import User_human

class User_human_Form(forms.ModelForm):
    class Meta:
        model = User_human
        fields = ('second_name','real_name')