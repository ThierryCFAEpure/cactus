# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
  email = forms.EmailField(label='Courriel :')
  password = forms.CharField(label='Mot de passe :', widget = forms.PasswordInput)

  def clean(self):
    cleaned_data = super(LoginForm, self).clean()
    email = cleaned_data.get("email")
    password = cleaned_data.get("password")

    # Vérifie que les deux champs sont valides
    if email and password:
        result = User.objects.filter(email=email,password=password)
        if len(result) != 1:
            raise forms.ValidationError("Courriel inexistant ou mot de passe erroné." + email + " " + password)

    return cleaned_data
