
from django.contrib import admin
from django.urls import path, include
from .views import CreateBatch,AddToko

from django.conf import settings 
from django.conf.urls.static import static 

urlpatterns = [
    path('create_batch/', CreateBatch.as_view(), name='create_batch'),
    path('add_toko/', AddToko.as_view(), name='add_toko'),
] 

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)