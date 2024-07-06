
from django.db import models

# Create your models here.

class Blog(models.Model):
    name  = models.CharField(max_length=50)
    blog_name = models.CharField(max_length=200,default = 'null')
    content = models.TextField(max_length=500)
