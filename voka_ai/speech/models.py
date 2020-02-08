from django.db import models

# Create your models here.

class RequestItem(models.Model):
    user_email = models.EmailField(max_length=255)
    link = models.CharField(max_length=2048)
    text = models.TextField()
    date = models.DateField(auto_now_add=True)