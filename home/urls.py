from django.urls import path
from .views import HomeView, CategoryView,AddPostView,DetailPostView,DeletePostView,UpdatePostView,AddCategoryView,LikeView
from django.conf import settings 
from django.conf.urls.static import static 


urlpatterns = [
    path('',HomeView.as_view(), name='home',),
    path('category/<int:pk>/', CategoryView.as_view(), name='category'),
    path('add_post/', AddPostView.as_view(), name='add-post'),
    path('detail_post/<slug:slug>/', DetailPostView.as_view() , name='detail-post'),
    path('delete_post/<slug:slug>/remove/', DeletePostView.as_view() , name='delete-post'),
    path('edit_post/<slug:slug>/', UpdatePostView.as_view(), name='update-post'),
    path('add_category/', AddCategoryView.as_view(), name='add-category'),
    path('like/<str:slug>', LikeView, name='like_post'),
] 
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)