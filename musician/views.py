from django.shortcuts import render, redirect
from django.contrib import messages
from . import forms
from django.contrib.auth.forms import  AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from . import models
from django.views import View

# Create your views here.
# Function based views:
# @login_required
# def add_musician(request):
#     if request.method == 'POST':
#         musician_form = forms.MusicianForm(request.POST)
#         if musician_form.is_valid():
#             musician_form.save()
#             return redirect('add_musician')
    
#     else:
#         musician_form = forms.MusicianForm()
#     return render(request, 'add_musician.html', {'form' : musician_form})

# def register(request):
#     if request.method == 'POST':
#         register_form = forms.RegistrationForm(request.POST)
#         if register_form.is_valid():
#             register_form.save()
#             messages.success(request, 'Account Created Successfully')
#             return redirect('register')
    
#     else:
#         register_form = forms.RegistrationForm()
#     return render(request, 'register.html', {'form' : register_form, 'type' : 'Register'})



# def user_login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, request.POST)
#         if form.is_valid():
#             user_name = form.cleaned_data['username']
#             user_pass = form.cleaned_data['password']
#             user = authenticate(username=user_name, password=user_pass)
#             if user is not None:
#                 messages.success(request, 'Logged in Successfully')
#                 login(request, user)
#                 return redirect('homepage')
#             else:
#                 messages.warning(request, 'Login information incorrect')
#                 return redirect('register')
#     else:
#         form = AuthenticationForm()
#         return render(request, 'register.html', {'form' : form, 'type' : 'Login'})



# @login_required
# def user_logout(request):
#     logout(request)
#     return redirect('user_login')



# Class based views:


@method_decorator(login_required, name='dispatch')
class AddMusicianCreateView(CreateView):
    model = models.Musician
    form_class = forms.MusicianForm
    template_name = 'add_musician.html'
    success_url = reverse_lazy('add_musician')
    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Musician Added Successfully')
        return super().form_valid(form)
    


class UserRegisterView(View):
    template_name = 'register.html'

    def get(self, request, *args, **kwargs):
        register_form = forms.RegistrationForm()
        return render(request, self.template_name, {'form': register_form, 'type': 'Register'})

    def post(self, request, *args, **kwargs):
        register_form = forms.RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Account Created Successfully')
            return redirect('user_register')
        return render(request, self.template_name, {'form': register_form, 'type': 'Register'})




class UserLoginView(LoginView):
    template_name = 'register.html'

    def get_success_url(self):
        return reverse_lazy('homepage')

    def form_valid(self, form):
        messages.success(self.request, 'Logged in successfully')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request, 'Logged in information incorrect')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context
    



class UserLogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        messages.success(self.request, 'Logged out successfully')
        return redirect('user_login')