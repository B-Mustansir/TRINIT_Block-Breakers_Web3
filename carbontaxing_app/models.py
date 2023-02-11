from django.db import models

# Create your models here.
class carbonEmmited(models.Model):
    company_name = models.CharField(max_length=100)
    carbon_emmited_CO2 = models.IntegerField(default=0)
    carbon_emmited_CH4 = models.IntegerField(default=0)
    carbon_emmited_N2O = models.IntegerField(default=0)
    carbon_emmited_F = models.IntegerField(default=0)
    carbon_emmited_Total = models.IntegerField(default=0)
    year=models.IntegerField(default=0)
    public_key=models.CharField(max_length=100,default="null")
    
    
class carbonCap(models.Model):
    sector_name = models.CharField(max_length=100)
    cap_alloted = models.IntegerField()

