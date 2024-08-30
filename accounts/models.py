from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

# Create your models here.
class Users(AbstractUser):
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    phone = models.CharField(validators = [phoneNumberRegex], max_length = 16, unique = True)
    update_at = models.DateTimeField(auto_now_add=True)