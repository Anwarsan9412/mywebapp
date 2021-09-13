# https://colinkingswood.github.io/Model-Form-Customisation/

from django.forms import ModelForm, fields 
from .models import Profile, Post, Category
from django.forms.models import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget
from crequest.middleware import CrequestMiddleware

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user_profile']
        
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = '__all__'
        exclude = ['username','email','password1','password2']
        
        
class PostForm(ModelForm):  
    username = forms.Select(attrs={'class':'form-control', 'type':'hiden'}),
    judul = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'form-control'}))
    category = forms.ModelChoiceField(queryset=Category.objects.all(),required=True,widget=forms.Select(attrs={'class':'form-control'}))
    # author = forms.ModelChoiceField(queryset=Profile.objects.all(),required=True,widget=forms.Select(attrs={'class':'form-control','type':'hiden'}))
    author = forms.Select(attrs={'class':'form-control', 'type':'hiden'}),
    body = forms.CharField(widget=CKEditorWidget(attrs={'class':'form-control'}))
    is_published = forms.NullBooleanField(
        label="Is Publish ",
        required=False,
        initial=True,
        widget=forms.Select(attrs={'class':'form-control'},choices=[
                               (True, "Yes"),
                               (False, "No")]))
    
    class Meta:
        model = Post 
        fields = '__all__'
        exclude = ['published','update','slug','author','username','likes']

class CategoryForm(ModelForm):
    category = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = Category
        fields = '__all__'
        exclude = ['slug']
        

class UpdatePostForm(ModelForm):  
    def __init__(self, *args, **kwargs):
        super(UpdatePostForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        
    class Meta:
        model = Post 
        fields = '__all__'
        exclude = ['published','update','slug','author','likes','username']