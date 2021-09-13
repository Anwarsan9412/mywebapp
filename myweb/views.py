from django.views.generic import TemplateView, ListView, DetailView, View, CreateView, DeleteView,UpdateView
from home.models import Post
from home.forms import PostForm
from accounts.decorators import allowed_users
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from django.contrib.messages.views import SuccessMessageMixin
# from sweetify.views import SweetifySuccessMixin
# import sweetify




@method_decorator([login_required,allowed_users(allowed_roles=['user','admin'])], name='dispatch')  
class AddPostView(SuccessMessageMixin,CreateView):
    # permission_required = 'home.add_post'
    template_name = "add_post.html"
    model = Post
    # fields = '__all__'
    form_class = PostForm
    success_message = 'Added Successfully!'
    