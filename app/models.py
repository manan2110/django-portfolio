from django.db import models

# Create your models here.


class DP(models.Model):
    picture = models.ImageField(upload_to='images')


class Profile(models.Model):
    line1 = models.CharField(max_length=100)
    line2 = models.CharField(max_length=100)
    line3 = models.CharField(max_length=100)
    line4 = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=256)


class Project(models.Model):
    name = models.CharField(max_length=256)
    desc = models.CharField(max_length=512)
    github_link = models.URLField()
