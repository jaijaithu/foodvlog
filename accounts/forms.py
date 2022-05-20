from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NewUserForm(UserCreationForm):
    firstname = forms.CharField(max_length=250)
    lastname = forms.CharField(max_length=250)
    username = forms.CharField(max_length=250)
    email = forms.EmailField(required=True)
    psw = forms.IntegerField()
    confirmpsw = forms.IntegerField()

    class Meta:
        model = User
        fields = ("firstname", "lastname", "username", "email", "psw", "confirmpsw")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
