from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    pass
    points = models.PositiveIntegerField(("points"))
    
class UserHistory(models.Model):
    uid = models.IntegerField()
    wpid = models.IntegerField()
    Sucess = models.BooleanField()
    time = models.DateTimeField()
   

class Sample(models.Model):
    fid =  models.IntegerField()
    name = models.TextField(default="")
    id = models.AutoField(primary_key=True)
    
    def __str__(self):
        return ' fid:{}  \n name:{}\n'.format(self.fid, self.name)


