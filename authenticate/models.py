from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator,MinLengthValidator

from locations.models import City

class User(AbstractUser):
    first_name=None
    last_name=None
    email=None
    is_staff =None
    last_login = None
    USER_TYPE_CHOICES = (
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('user','User')
    )
    username = models.CharField(unique=True,max_length=50)
    password = models.CharField(max_length=255,validators=[MinLengthValidator(8)])
    phone_number = models.CharField(unique=True,max_length=10,validators=[RegexValidator(regex='^\d{10}$',message='Phone number must be exactly 10 digits.',code='nomatch')])
    user_type = models.CharField(max_length=10,choices=USER_TYPE_CHOICES,default='User')
    is_active = models.BooleanField(default=False)
     
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True)
   
    
    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        