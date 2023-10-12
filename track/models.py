from django.db import models
from django.contrib.auth.models import User





type=(
 ('postive','postive'),
 ('negative','negative')
)
class Profile(models.Model):
 user=models.ForeignKey(User,on_delete=models.CASCADE)
 income=models.FloatField()
 expenses=models.FloatField(default=0)
 balance=models.FloatField(null=True)


# Create your models here.
class Expenses(models.Model):
 user=models.ForeignKey(User,on_delete=models.CASCADE)
 name=models.CharField(max_length=200)
 type=models.CharField(max_length=200,choices=type)
 amount=models.FloatField(default=0)
 def __str__(self) :
  return self.name