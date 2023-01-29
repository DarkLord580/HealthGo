from django.contrib.auth.models import AbstractUser
from django.db import models



class User(models.Model):
    UID = models.AutoField(primary_key=True)
    UserID = models.CharField(max_length=128)
    Username = models.CharField(max_length=128)
    Password = models.CharField(max_length=128)
    points = models.IntegerField(default=0)

class Sample(models.Model):
    fid =  models.IntegerField()
    name = models.TextField(default="")
    id = models.AutoField(primary_key=True)
    
    def __str__(self):
        return ' fid:{}  \n name:{}\n'.format(self.fid, self.name)


