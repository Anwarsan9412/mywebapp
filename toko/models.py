from django.db import models
from django.utils import timezone
from django.urls import reverse_lazy,reverse


class Passsql(models.Model):
    password = models.CharField(unique=True,max_length=250)
    bln = models.CharField(unique=True,max_length=200)

    def __str__(self):
        return self.password
    
    def get_absolute_url(self):
        # return reverse('article-detail', args= (str(self.id)))
        return reverse('create_batch')

class Cabang(models.Model):
    cabang = models.CharField(unique=True,max_length=10)

    def __str__(self):
        return self.cabang
    
    def get_absolute_url(self):
        # return reverse('article-detail', args= (str(self.id)))
        return reverse('create_batch')

class Toko(models.Model):
    cabang = models.ForeignKey(Cabang, on_delete=models.CASCADE)
    kdtk = models.CharField(max_length=10,unique=True, null=True)
    nama_toko = models.CharField(max_length=200, null=True)
    ip = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.kdtk

    def get_absolute_url(self):
        # return reverse('article-detail', args= (str(self.id)))
        return reverse('create_batch')
