from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    
    username = models.CharField(
        max_length=150,
        validators=[AbstractUser.username_validator],
        unique=True,
        null=True,
        blank=True
    )
    
    email = models.EmailField(
        unique=True
    )
    
    role = models.CharField(
        max_length=10, 
        choices=[('subscriber', 'Subscriber'), ('author', 'Author')]
    )
    
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "role",]