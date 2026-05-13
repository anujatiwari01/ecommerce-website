from django .forms import ModelForm
from django.contrib.auth.models import User

from django import forms

class UserCreationForm(ModelForm):
    password1=forms.CharField(label='Password',widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username','email','password','password1']

    def clean(self):
        cleaned_data=super().clean()
        password1=cleaned_data.get('password')
        password2=cleaned_data.get('password1')            

        if password1 != password2:
            raise forms.ValidationError("Password does not match")              
        return self.cleaned_data
    
    def save(self, commit=True):
        user=super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
    
class UserLoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)