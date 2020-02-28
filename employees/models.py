from django.db import models
from django.contrib.auth.models import AbstractUser

class Employee(AbstractUser):
    registration = models.IntegerField(default=123)

    def __str__(self):
        return self.username


