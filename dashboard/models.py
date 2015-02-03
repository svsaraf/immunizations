from django.db import models

class Patient(models.Model):
	name = models.CharField(max_length=1000, default="")
	patientid = models.IntegerField(default=0)

class Immunization(models.Model):
    name = models.CharField(max_length=1000, default="")
    number = models.IntegerField(default=1)
    immunizationid = models.IntegerField(default=0)

class ImmunizationRecord(models.Model):
	patient = models.ForeignKey(Patient)
	immunization = models.ForeignKey(Immunization)
	date = models.DateTimeField(auto_now_add=True)
	
# Create your models here.
