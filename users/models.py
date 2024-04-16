from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.CharField(max_length=127, unique=True)
    birthdate = models.DateField(null=True, blank=True, default=None)
    is_employee = models.BooleanField(default=False)
    
