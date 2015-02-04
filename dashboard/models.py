from django.db import models

class Patient(models.Model):
	name = models.CharField(max_length=1000, default="")
	patientid = models.IntegerField(unique=True)
	age = models.DecimalField(max_digits=5, decimal_places=2, null=True)
	dob = models.DateTimeField()

	def __str__(self):
		return self.name + " with id " + str(self.patientid)

class Immunization(models.Model):
    name = models.CharField(max_length=1000, default="")
    number = models.IntegerField(default=1)
    immunizationid = models.IntegerField(default=0, unique=True)
    recommended_age = models.DecimalField(max_digits=5, decimal_places=2)
    catchup_age = models.DecimalField(max_digits=5, decimal_places=2, default=12)

    def __str__(self):
    	return str(self.immunizationid) + ":" + self.name + " is number " + str(self.number)

class ImmunizationRecord(models.Model):
	patient = models.ForeignKey(Patient)
	immunization = models.ForeignKey(Immunization)
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.patient) + str(self.immunization) + str(self.date)

# Create your models here.
