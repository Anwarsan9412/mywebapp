from django.contrib.auth.models import Group
from django.http import request
from django.shortcuts import redirect, render
from django.views import generic
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic import View
from django.views.generic.edit import CreateView
from .forms import SignUpForm,PasswordChangingForm,EditProfileForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from home.models import Profile
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.views import PasswordChangeView,LoginView
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user,admin_only, allowed_users

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from home.forms import ProfileForm

from django.contrib.messages.views import SuccessMessageMixin
# import sweetify

@method_decorator([unauthenticated_user],name='dispatch')
class LoginFormView(SuccessMessageMixin, LoginView):
    template_name='registration/login.html'
    success_url = reverse_lazy('home')
    # success_message = "You were successfully logged in."
    success_message = "%(username)s, You were successfully logged in"
    error_message = "Failed Login"
    def form_invalid(self, form):
        messages.error(self.request, self.error_message)
        return super().form_invalid(form)
    

class PasswordChangeView(SuccessMessageMixin,PasswordChangeView):
    # form_class = PasswordChangeForm
    template_name='registration/change_password.html'
    form_class = PasswordChangingForm
    success_url = reverse_lazy('logout')
    success_message = "Please Login"
    error_message = "Failed to Change Password"

@method_decorator([login_required], name='dispatch') 
class UserRegisterView(SuccessMessageMixin,generic.CreateView):
    # form_class = UserCreationForm
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    success_message = "%(username)s was created successfully"
    permission_denied_message = 'You have to be logged in to access that page'
 
        
    def form_valid(self, form):
        response = super().form_valid(form)  # self.object gets saved here, and the response is a `HttpResponseRedirect`
        post = self.request.POST.get('group')
        groups = Group.objects.get(id=post)
        self.object.groups.add(groups)
        Profile.objects.create(
            user_profile=self.object,
            username=self.object.username,
            first_name = self.object.first_name,
            last_name = self.object.last_name,
            email=self.object.email,
        )
        # yg atas di pindah ke signals.py
        return response  # don't forget to return the response

@method_decorator([login_required,allowed_users(allowed_roles=['user','admin'])], name='dispatch')   
class AccountSetting(View):
    template_name ='registration/account_setting.html'
    success_message = "%(username)s was created successfully"
    # form_class= EditProfileForm
    
    def get(self, request):
        profile = self.request.user.profile
        form = ProfileForm(instance=profile)  
        return render(request,self.template_name, {'form':form})
    
    def post(self, request):
        profile = self.request.user.profile
        form = ProfileForm( self.request.POST, self.request.FILES, instance=profile)
        if form.is_valid(): 
            User.objects.filter(id=profile.user_profile_id).update(
            username=profile.username,
            first_name=profile.first_name,
            last_name=profile.last_name,
            email=profile.email,
             ) 
            # messages.success(self.request, "Profile updated successfully!")   
            messages.success(self.request, f"{self.request.user.first_name} {self.request.user.last_name}, Profile updated successfully!")  
            form.save()
        else:
            messages.error(request, f"{self.request.user.first_name} {self.request.user.last_name}, It didn't save!")
        return render(request,self.template_name, {'form':form})