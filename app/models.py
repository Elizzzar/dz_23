from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class User_human(models.Model):
    second_name = models.CharField(max_length=48)
    real_name = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.second_name
    class Meta:
        abstract = True