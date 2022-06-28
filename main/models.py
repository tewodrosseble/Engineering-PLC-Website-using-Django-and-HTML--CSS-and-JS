from django.db import models
from django.forms import ImageField


class Blog(models.Model):
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to="media/posted")
    body =models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    auther = models.ForeignKey("auth.User", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Gallery(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to="media/gallery")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Services(models.Model):
    image = models.ImageField(upload_to='media/services')
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Coverphoto(models.Model):
    image = models.ImageField(upload_to="media/coverphoto")
    title = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Reference (models.Model):
    id = models.Index
    title  = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media/reference')
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Certificate(models.Model):
    title = models.CharField(max_length=220)
    image = models.ImageField(upload_to='media/certificates')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Video(models.Model):
    title = models.CharField(max_length=220)
    video = models.FileField(upload_to='media/videos')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class videos(models.Model):
    video_id = models.CharField(blank=False, max_length=32)
    file_name = models.CharField(blank=False, max_length=500)
    # def __str__(self):
    #     return self.id