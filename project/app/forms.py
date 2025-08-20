from django import forms
from .models import *
from django.core.exceptions import ValidationError

# class studentform(forms.ModelForm):
#     class Meta:
#         model =student
#         fields ='__all__'

class loginform(forms.ModelForm)  :
    class Meta:
        model =student
        fields =['email','passw']






class studentform(forms.ModelForm):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    document = forms.FileField()
    image = forms.ImageField()
    vedioo=forms.FileField()
    passw=forms.CharField()
    c_passw=forms.CharField()
    
    class Meta:
        model = student
        fields = '__all__'

    def clean(self):
        super().clean()
        print(super().clean())
        print(self.cleaned_data.get('name'))
        print(self.cleaned_data.get('email'))
        print(self.cleaned_data.get('document'))
        print(self.cleaned_data.get('image'))
        print(self.cleaned_data.get('passw'))
        print(self.cleaned_data.get('c_passw'))
        return self.cleaned_data

    def clean_name(self):
        name = self.cleaned_data.get('name')
        print(name)
        print(type(name))
        if len(name) == 0:
            raise ValidationError("Name field cannot be Empty.")
        elif name.isdigit():
            raise ValidationError("Name should not contain number.")
        elif name[0].isdigit():
            raise ValidationError("Name should not start with a number.")
        elif not (name.isalpha() and len(name) < 20 and len(name) > 3):
            raise ValidationError("Name should only contain letters and be between 4 to 20 letters.")
        return name
