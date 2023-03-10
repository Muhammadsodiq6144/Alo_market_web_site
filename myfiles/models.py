from django.db import models

# Create your models here.
class Type(models.Model):
    nomi = models.CharField(max_length=40)
    def __str__(self):
        return self.nomi
class Portfolio(models.Model):
    nomi = models.CharField(max_length=30)
    company_name = models.CharField(max_length=50)
    date = models.DateField()
    url = models.URLField()
    malumot = models.TextField()
    tur = models.ForeignKey(Type,on_delete=models.CASCADE)
    rasm1 = models.ImageField(upload_to='media')
    rasm2 = models.ImageField(upload_to='media', null=True,blank=True)
    rasm3 = models.ImageField(upload_to='media', null=True,blank=True)

class Services(models.Model):
    nomi = models.CharField(max_length=40)
    malumot = models.TextField()
    rasm = models.ImageField(upload_to='media')

class Team(models.Model):
    rasm = models.ImageField(upload_to='media')
    ismi = models.CharField(max_length=40)
    lavozimi = models.CharField(max_length=20)
    malumot = models.TextField()
    link1 = models.CharField(max_length=100)
    link2 = models.CharField(max_length=100)
    link3 = models.CharField(max_length=100)
    link4 = models.CharField(max_length=100)

class Murojaat(models.Model):
    name = models.CharField(max_length=40)
    mail = models.EmailField(max_length=65)
    title = models.CharField(max_length=40)
    text = models.TextField()
    date = models.DateField()

class Obunamail(models.Model):
    mail = models.EmailField(max_length=65)