from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User 
from django.utils.text import slugify
from django.conf import settings
from django.utils import timezone


from crequest.middleware import CrequestMiddleware
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class Category(models.Model):
    category = models.CharField(unique=True,max_length=255)
    slug  = models.SlugField(unique=True,blank=True, editable=False,max_length=255)
    data_created = models.DateTimeField(auto_now_add=True, null=True)
    
    def save(self):
        self.slug = slugify(self.category)
        super(Category, self).save()

    def __str__(self):
        return self.category
    
    def get_absolute_url(self):
        # return reverse('article-detail', args= (str(self.id)))
        return reverse('add-category')

class Profile(models.Model):
    user_profile = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=200, null=True)
    first_name = models.CharField(max_length=200,null=True,blank=True)
    last_name = models.CharField(max_length=200,null=True,blank=True)
    email = models.EmailField(null=True)
    profile_pic = models.ImageField(default='images/profile/profil.png' ,null=True, blank=True,upload_to='images/profile/' )
    data_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.username

class Post(models.Model):
    # username = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    username = models.ForeignKey(settings.AUTH_USER_MODEL,null=True,on_delete=models.CASCADE)
    # username = models.CharField(max_length=255,blank=True, null=True, editable = False)
    judul = models.CharField(unique=True,max_length=255)
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, models.PROTECT)
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    body = RichTextUploadingField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='blog_posts')
    created       = models.DateTimeField(auto_now_add=True)
    update      = models.DateTimeField(auto_now=True)
    is_published = models.NullBooleanField(default=True)
    published     = models.DateTimeField(null=True)
    slug        = models.SlugField(unique=True,editable=False,max_length=255)
    
    
    
    def save(self):
        self.slug = slugify(self.judul)
        current_request = CrequestMiddleware.get_request()
        users = current_request.user
        self.username = users
        self.author = Profile.objects.get(user_profile_id=users)      
        super(Post, self).save()

        if self.is_published == True:
            self.published = timezone.now()
        else:
            self.published == None      
        super().save()
        
    def total_likes(self):
        return self.likes.count()
    
    def __str__(self):
        return self.judul + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        # return reverse('article-detail', args= (str(self.id)))
        return reverse('home')
