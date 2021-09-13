from django.contrib.messages.api import error
from django.forms import widgets
from django.shortcuts import render,redirect
from django.views.generic import TemplateView, ListView, DetailView, View, CreateView, DeleteView,UpdateView
from .models import Category, Profile, Post
from django.urls import reverse_lazy,reverse
from accounts.decorators import unauthenticated_user,admin_only, allowed_users
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .forms import PostForm, CategoryForm, UpdatePostForm
from django.db.models import Q
from django.http import HttpResponseRedirect
from .filter import PostFilter
from django.core.paginator import Paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
# from sweetify.views import SweetifySuccessMixin
# import sweetify

from django.db import connection



def LikeView(request, slug):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
        messages.success(request, f"{request.user.first_name} {request.user.last_name}, You Do Not like It")
    else:
        post.likes.add(request.user)
        liked = True
        messages.success(request, f"{request.user.first_name} {request.user.last_name} , You Like It")
    return HttpResponseRedirect(reverse('detail-post', args=[str(slug)]))


@method_decorator([login_required], name='dispatch') 
class HomeView(ListView):
    template_name = "index.html"
    model = Post
    ordering =['-published']
    fields = '__all__'
    # paginate_by = 2
    # queryset = Post.objects.filter(Q(username_id=7)|Q(is_published=1))
    
    def get_queryset(self):
        curren_user = self.request.user
        posts = Post.objects.all()
        all = posts.filter(Q(username_id=curren_user)|Q(is_published=1)).order_by('-update')      
        #print(all)
        return all


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categori = Category.objects.all().order_by('category')
        myFilter = PostFilter(self.request.GET, queryset= self.get_queryset())
        posts_filter = myFilter.qs
        
        context["category"] = categori
        context["all"] = posts_filter
        context['myFilter'] = myFilter

        return context
    
@method_decorator([login_required,allowed_users(allowed_roles=['user','admin'])], name='dispatch') 
class CategoryView(TemplateView):
    model = Category
    template_name = 'categories.html'
    def get_context_data(self, *args, **kwargs):
        pk = kwargs.get('pk')
        curren_user = self.request.user
        cate = Category.objects.filter(id=pk).values("category").distinct()
        # cat = Post.objects.filter(category_id=pk)
        posts = Post.objects.all()
        cat = posts.filter(Q(username_id=curren_user)|Q(is_published=1),category_id=pk)
        context = {
            'title': 'sosmed memakai Class-based view',
            'cat' : cat,
            'cate': cate
     
        }
        return context


@method_decorator([login_required,allowed_users(allowed_roles=['user','admin'])], name='dispatch')  
class AddPostView(SuccessMessageMixin,CreateView):
    # permission_required = 'home.add_post'
    template_name = "add_post.html"
    model = Post
    # fields = '__all__'
    form_class = PostForm
    success_message = 'Added Successfully!'
    

    
@method_decorator([login_required,allowed_users(allowed_roles=['admin','user'])], name='dispatch')
class DetailPostView(DetailView):
    template_name = 'detail_post.html'
    model =  Post
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        stuff = get_object_or_404(Post, slug=self.kwargs['slug'])
        total_likes = stuff.total_likes()
        # print(stuff)
        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        context["total_likes"] = total_likes    
        context['liked'] = liked
        return context
    

@method_decorator([login_required,allowed_users(allowed_roles=['user','admin'])], name='dispatch') 
class DeletePostView(SuccessMessageMixin,DeleteView):    
    template_name = 'delete_post.html'
    model =  Post
    success_url = reverse_lazy('home')
    success_message = 'Deleted Successfully!'
    

@method_decorator([login_required,allowed_users(allowed_roles=['user','admin'])], name='dispatch')    
class UpdatePostView(SuccessMessageMixin,UpdateView):
    # permission_required = 'home.update_post'
    model = Post
    form_class = UpdatePostForm
    template_name ='update_post.html'
    success_message = 'Updated Successfully!'

@method_decorator([login_required,allowed_users(allowed_roles=['user','admin'])], name='dispatch')
class AddCategoryView(SuccessMessageMixin,CreateView):
    # permission_required = 'home.add_category'
    raise_exception = False
    template_name = "add_category.html"
    model = Category
    form_class = CategoryForm
    success_message = 'Added Successfully!'

    
    # messages.success(self.request, "Profile updated successfully!")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categori = Category.objects.all().order_by('category')

        context["category"] = categori
        return context