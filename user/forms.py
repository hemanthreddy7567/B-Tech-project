from django import forms
from django.core import validators

from manager.models import viewdetailsmodel
from user.models import users


def name_check(value):
    if value.isalpha()!=True:
        raise forms.ValidationError("only string are allowed")



class userForm(forms.ModelForm):
    firstname = forms.CharField(widget=forms.TextInput(), required=True, max_length=100,validators=[name_check])
    lastname = forms.CharField(widget=forms.TextInput(), required=True, max_length=100, validators=[name_check])
    email = forms.CharField(widget=forms.TextInput(), required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True, max_length=100)
    conformpassword = forms.CharField(widget=forms.PasswordInput(), required=True, max_length=100)
    mobileno = forms.CharField(widget=forms.TextInput(), required=True, max_length=10,validators=[validators.MaxLengthValidator(10),validators.MinLengthValidator(10)])
    city = forms.CharField(widget=forms.TextInput(), required=True, max_length=100,validators=[name_check])
    def __str__(self):
        return self.email

    class Meta:
        model = users
        fields=['firstname','lastname','email','password','conformpassword','mobileno','city']
    def clean(self):
        cleaned_data=super().clean()
        inputpassword=cleaned_data['password']
        inputconformpassword=cleaned_data['conformpassword']
        if inputpassword!=inputconformpassword:
            raise forms.ValidationError("password should be match")


class viewnewsdetailsform(forms.ModelForm):
    category = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}), required=True, max_length=100)
    title = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}), required=True, max_length=100)
    #description = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}), required=True, max_length=100)
    description = forms.CharField(widget=forms.Textarea(attrs={'readonly': 'readonly'}), required=True, max_length=100)
    location = forms.IntegerField(widget=forms.TextInput(attrs={'readonly': 'readonly'}), required=True)
    # file = forms.FileField(widget=forms.TextInput(attrs={'readonly': 'readonly'}), required=True, max_length=100)
    review = forms.CharField(widget=forms.Textarea(), required=True, max_length=100)

    class Meta:
        model = viewdetailsmodel
        fields = ('category', 'title', 'description', 'description', 'location','review')