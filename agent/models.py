from django.db import models


# Create your models here.
class Agent(models.Model):
    title = models.CharField(max_length=30)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    image = models.ImageField(upload_to='agent/images')
    skype = models.CharField(max_length=20)
    facebook_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name
