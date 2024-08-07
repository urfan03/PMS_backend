from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

class Worker(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    email = models.EmailField()
    image = models.ImageField(upload_to='workers/')

    def __str__(self):
        return self.name

class ServiceDetail(models.Model):
    LittleHeadName = models.CharField(max_length=20)
    LittleTextInfo = models.TextField(max_length=100)
    LargeHeadName = models.CharField(max_length=50)
    Image = models.ImageField(upload_to='images/')
    DetailHead = models.CharField(max_length=25)
    DetailText = models.TextField()

    def __str__(self):
        return self.LittleHeadName

class QrCode(models.Model):
    name = models.CharField(max_length=100)



