from rest_framework import serializers

from authenticate.models import User
from .models import Report
class ReportSerializer(serializers.ModelSerializer):
    REPORT_TYPE_CHOICES = [
        ('Electricity', 'Electricity'),
        ('Water', 'Water'),
        ('Roads', 'Roads'),
        ('Internet', 'Internet'),
        ('Sanitation', 'Sanitation'),
        ('Healthcare', 'Healthcare'),
        ('Education', 'Education'),
        ('Public_Safety', 'Public Safety'),
        ('Housing', 'Housing'),
        ('Transportation', 'Transportation'),
    ]
    user = serializers.PrimaryKeyRelatedField(queryset = User.objects.all())
    title = serializers.CharField(required = True)
    description = serializers.CharField(required = True)
    report_type = serializers.ChoiceField(required = True,choices=REPORT_TYPE_CHOICES)
    image = serializers.ImageField(required=False, allow_null=True)
    class Meta:
        model = Report
        fields = ['id', 'user', 'title', 'description', 'report_type', 'created_at','image']
        read_only_fields = ['user', 'created_at']
