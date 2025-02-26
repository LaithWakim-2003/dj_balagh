from rest_framework import serializers

from .models import Governorate, City

class GovernorateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Governorate
        fields = ['id', 'name']

class CitySerializer(serializers.ModelSerializer):
    governorate = serializers.PrimaryKeyRelatedField(queryset = Governorate.objects.all())
    class Meta:
        model = City
        fields = ['id', 'name', 'governorate']

