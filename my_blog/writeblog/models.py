from django.db import models
from app.models import Blogger
# Create your models here.


class BlogWrite(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=4000, null=True, blank=True)
    blog_img = models.ImageField(null= True, blank= True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Writer(models.Model):
    blog_writer = models.ForeignKey(Blogger, on_delete= models.CASCADE)
    myWrite = models.ManyToManyField(BlogWrite) 

    def __str__(self):
        return str(self.blog_writer.blogger)
    

