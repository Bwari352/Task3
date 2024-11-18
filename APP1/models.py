from django.db import models

# Create your models here.

class Services(models.Model):
    operation = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Services/')




    def __str__(self):
        return f"{self.operation} --- {self.image}"


class Posts(models.Model):
    date = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    type = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.date} --- {self.name}--- {self.description}--- {self.type}"

class Team(models.Model):
    full_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    profile_picture = models.FileField(upload_to='teams/')
    twitter_url = models.CharField(max_length=200)
    facebook_url = models.CharField(max_length=200)
    linkedin_url = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.full_name} --- {self.position}"



class Users(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return f"{self.name} --- {self.email}--- {self.subject}--- {self.message}"

