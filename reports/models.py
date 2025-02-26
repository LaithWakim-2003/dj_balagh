from django.db import models
from authenticate.models import User

class Report(models.Model):
    REPORT_TYPE_CHOICES = [
        ('electricity','Electricity'),
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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    report_type = models.CharField(max_length=50, choices=REPORT_TYPE_CHOICES)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
