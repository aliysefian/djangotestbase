from django.db import models
from django.db.models.fields import URLField
from django.utils.timezone import now
# Create your models here.
class Company(models.Model):
    class CompanyStatus(models.TextChoices):
        LAYOFF="layoff"
        HIRING_FREEZE="Hiring freez"
        HIRING="Hiring"

    name=models.CharField(max_length=100,unique=True)
    status=models.CharField(choices=CompanyStatus.choices,default=CompanyStatus.LAYOFF,max_length=20)
    last_update=models.DateTimeField(default=now,editable=True)
    application_link=URLField(blank=True)
    notes=models.CharField(max_length=100,blank=True)
    
