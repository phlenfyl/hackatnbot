from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser

from userauth.settings import UserSettings

# Create your models here.

ROLE_CHOICES = (
                ("student", "Student"), ("staff", "Staff"),
                ("non staff", "Non Staff"), ("non student", "Non Student")
                )

class User(AbstractUser):
    username = None
    role = models.CharField(max_length=12, error_messages={"required": "Role must be provided"})
    email = models.EmailField(
        unique=True, blank=False, error_messages={"unique": "A user with that email already exists."}
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    

    def __unicode__(self):
        return self.email
    
    objects = UserSettings()