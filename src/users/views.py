from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile
from .forms import CustomUserCreationForm

from .utils import searchProfiles

#function to login
def loginUser(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('pofiles')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request, 'Ce nom utilisateur est inexistant')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request,'Le nom utilisateur ou le mot de passe est incorrect')
    return render(request, 'users/login_register.html')

#function to logout
def logoutUser(request):
    logout(request)
    messages.info(request, 'Utilisateur déconnecté')
    return redirect('login')

#function to register a user
def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'Compte utilisateur créé avec succès!')
            #login de l'utilisateur juste après la création de compte
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, 'Erreur survenue lors de la création de Compte utilisateur!')
    context = {'page': page, 'form': form}
    return render(request, 'users/login_register.html', context)

def profiles(request):
    profiles, search_query = searchProfiles(request)
    context = {'profiles':profiles, 'search_query': search_query}
    return render(request, 'users/profiles.html', context)

def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    context = {'profile': profile}
    return render(request, 'users/user-profile.html', context)

#compte utilisateur
@login_required(login_url = "login")
def userAccount(request):
    profile = request.user.profile
    documents = profile.document_set.all()
    context = {'profile': profile, 'documents': documents} 
    return render (request, 'users/account.html', context)
