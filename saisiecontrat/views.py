# -*- coding: utf-8 -*-

from django.shortcuts import render,redirect
from datetime import datetime
from saisiecontrat.forms import LoginForm

def premierepage(request):
  return render (request,'premierepage.html', {'current_date_time': datetime.now})

def login(request):

    if len(request.POST) > 0:

        form=LoginForm(request.POST)
        if form.is_valid():
            return redirect('/premierepage')
        else:
            return render(request,'login.html',{'form':form})
    else:
        form = LoginForm()
        return render(request,'login.html',{'form':form})

#def login(request):
  # Test si formulaire a été envoyé
#  if len(request.POST) > 0:
    # Test si les paramètres attendus ont été transmis
#    if 'email' not in request.POST or 'password' not in request.POST:
#      error = "Veuillez entrer une adresse de courriel et un mot de passe."
#      return render(request,'login.html', {'error': error})
#    else:
#      email = request.POST['email']
#      password = request.POST['password']
      # Test si le mot de passe est le bon
#      if password != 'sesame' or email != 'pierre@lxs.be':
#        error = "Adresse de courriel ou mot de passe erroné."
#        return render(request,'login.html', {'error': error})
      # Tout est bon, on va à la page d'accueil
#      else:
#        return redirect('/premierepage')
  # Le formulaire n'a pas été envoyé
#  else:
#    return render (request,'login.html')
