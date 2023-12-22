from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.views import LogoutView, LoginView, PasswordChangeView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth import login,logout, authenticate
from .forms import RegisterUserForm
from .models import Profile
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic import TemplateView, View
from django.urls import reverse_lazy
from .forms import ProfileForm, UserForm


class HandledPermissionView(TemplateView):
    template_name='account/authenticated.html'


class LoginFormView(UserPassesTestMixin,LoginView):
    template_name= 'account/login.html'
    
    def test_func(self):
        return not self.request.user.is_authenticated
    
    def handle_no_permission(self):
        return redirect('/account/authenticated')

    def get_context_data(self,**kwargs):
        messages.add_message(self.request,level=messages.SUCCESS, message="Haz iniciado sesion!")
        context = super().get_context_data(**kwargs)
        context['title'] = 'Iniciar Sesion'
        return context
    


class RegisterUser(UserPassesTestMixin,FormView):
    template_name = 'account/register.html'
    form_class = RegisterUserForm
    fields = ['username','password1','password2']
    redirect_autheticated_user = True
    success_url = '/'

    def test_func(self):
        return not self.request.user.is_authenticated
    
    def handle_no_permission(self):
        return redirect('/account/authenticated')

    def post(self,request):
        user_creation_form = RegisterUserForm(request.POST)
        if user_creation_form.is_valid():
            user_creation_form.save()
            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request,user)
            messages.add_message(self.request,level=messages.SUCCESS, message="¡Gracias por Registrarte! Bienvenido/a!")
            return redirect('core:index')
        data= {
            'form': user_creation_form
        }
        return render(request, 'account/register.html', data)
    
class ProfileView(TemplateView):
    template_name= 'account/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['user_form'] = UserForm(instance=user)
        context['profile_form'] = ProfileForm(instance=user.profile)
        return context
    
    def post(self, request, *args, **kwargs):
        user = self.request.user
        user_form = UserForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=user.profile)


        if user_form.is_valid() or profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('/account/profile')
        
        context = self.get_context_data()
        context['user_form'] = user_form
        context['profile_form'] = profile_form
        return render(request, 'account/profile.html', context)


class ChangePasswordFormView(PasswordChangeView):
    template_name = 'account/changed_password.html'
    success_url = '/account/profile/'

    def form_valid(self, form):
        messages.success(self.request, 'Tu contraseña se modifico Exitosamente!')
        return super().form_valid(form)