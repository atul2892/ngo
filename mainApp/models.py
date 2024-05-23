from django.db import models
from ckeditor.fields import RichTextField


class BlogPost(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=1000)
    content = RichTextField()
    date = models.DateField(auto_now=False)
    image = models.ImageField(upload_to="uploads/")

    def __str__(self):
        return str(self.id)+" "+self.title
    
class EventPost(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=1000)
    content = RichTextField()
    date = models.DateField(auto_now=False)
    image = models.ImageField(upload_to="uploads/")

    def __str__(self):
        return str(self.id)+" "+self.title
    
class Gallery(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to="uploads/")

    def __str__(self):
        return str(self.id)
    
class ContactDetail(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(default="",null="true",blank="true")
    company = models.CharField(max_length=200,default="",null="true",blank="true")
    message = models.TextField(default="",null="true",blank="true")

    def __str__(self):
        return str(self.id)+" "+self.name
    
class NewsletterSubscription(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(default="",null="true",blank="true")
    
    def __str__(self):
        return str(self.id)+" "+self.email
