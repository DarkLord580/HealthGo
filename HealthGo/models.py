from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class User(AbstractUser):
    points = models.PositiveIntegerField(("points"))

class Sample(models.Model):
    fid =  models.IntegerField()
    name = models.TextField(default="")
    id = models.AutoField(primary_key=True)
    
    def __str__(self):
        return ' fid:{}  \n name:{}\n'.format(self.fid, self.name)


