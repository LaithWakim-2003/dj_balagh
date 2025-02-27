from rest_framework import serializers
from django.core.validators import RegexValidator,MinLengthValidator
from authenticate.models import User
from locations.models import City
from locations.serializers import CitySerializer

class UserSerializer(serializers.ModelSerializer):
    USER_TYPE_CHOICES = (
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('user','User')
    )
    username = serializers.CharField(required = True)
    password = serializers.CharField(write_only=True,required = True, max_length=255,validators=[MinLengthValidator(8)])
    phone_number = serializers.CharField(required = True, max_length=10,validators=[RegexValidator(regex='^\d{10}$',message='Phone number must be exactly 10 digits.',code='nomatch')])
    user_type = serializers.ChoiceField(required = True,choices = USER_TYPE_CHOICES)
    city = serializers.PrimaryKeyRelatedField(queryset=City.objects.all())
    class Meta:
        model = User
        fields = ['id','phone_number','username','user_type','date_joined','password','city']
        
class LoginSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(required = True, max_length=10,validators=[RegexValidator(regex='^\d{10}$',message='Phone number must be exactly 10 digits.',code='nomatch')])
    password = serializers.CharField(required = True, max_length=255,validators=[MinLengthValidator(8)])
    class Meta:
        model = User
        fields = ['id','phone_number','password']
        