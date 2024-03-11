from django.db import models

# Create your models here.
class BlogUser(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.email
