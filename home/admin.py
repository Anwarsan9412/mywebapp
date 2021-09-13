from django.contrib import admin
from .models import Profile, Post, Category

admin.site.register(Profile)

admin.site.register(Category)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    exclude = ('username','author','likes','published')

