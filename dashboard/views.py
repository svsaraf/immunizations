from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from dashboard.models import Patient, Immunization, ImmunizationRecord
import json as simplejson
import math
from django.http import HttpResponseRedirect, HttpResponse
import requests
from datetime import datetime

def home(request):
    context = RequestContext(request)
    pats = Patient.objects.all()
    num = 0
    for p in pats:
    	recs = len(ImmunizationRecord.objects.filter(patient=p))
    	imms = len(Immunization.objects.filter(recommended_age__lte=p.age))
    	if recs < imms:
    		num = num + 1
    return render_to_response('dashboard/home.html', {'out_of_date': num}, context)

def is_number(number):
	try:
		float(number)
		return True
	except:
		return False

def addimmunizations(request):
	context = RequestContext(request)

	if request.method == 'POST':
		print "Warning: Not checking or sanitizing input."
		id_number = request.POST['id_number']
		name_vaccine = request.POST['name_vaccine']
		number = request.POST['number']
		recommended_age = request.POST['recommended_age']
		catchup_age = request.POST['catchup_age']

		if is_number(id_number):
			if is_number(number):
				if is_number(recommended_age):
					if is_number(catchup_age):
						record = Immunization(name=name_vaccine, number=number, immunizationid=id_number, recommended_age=recommended_age, catchup_age=catchup_age)
						record.save()

		return HttpResponseRedirect("/add/")

	immune_list = Immunization.objects.all()
	for obj in immune_list:
		if obj.recommended_age < 1:
			obj.recommended_age = str(math.trunc(obj.recommended_age*12)) + " months"
		else:
			obj.recommended_age = str(obj.recommended_age) + " years"
	return render_to_response('dashboard/add.html', {'immune_list': immune_list}, context)

def addpatients(request):
	context = RequestContext(request)
	if request.method == 'POST':
		id_number = request.POST['id_number']
		name = request.POST['name']
		age = request.POST['age']
		patient = Patient(patientid=id_number, name=name, age=age)
		patient.save()
		return HttpResponseRedirect('/patients/')
	patient_list = Patient.objects.all()
	for obj in patient_list:
		if obj.age < 1:
			obj.age = str(math.trunc(obj.age*12)) + " months"
		else:
			obj.age = str(obj.age) + " years"

	return render_to_response('dashboard/patients.html', {'patient_list': patient_list}, context)
# Create your views here.

def addfromapi(request):
	headers = {'Authorization': 'Bearer C8BJIYgfI23ZusS8rQpANFjHBkkTCE',}
	domain = 'https://drchrono.com'
	patients = []
	patients_url = '/api/patients'
	while patients_url:
		data = requests.get(domain + patients_url, headers = headers).json()
		patients.extend(data['results'])
		patients_url = data['next']

	for p in patients:
		n = p['first_name'] + p['last_name']
		newt = Patient(name=n,age=1,patientid=str(p['id']))
		newt.save()

	return HttpResponseRedirect("/")

	#for patient in patients:


def addimmuno(request):
	if request.method == 'POST':
		id_number = request.POST['pat_id']
		imm_name = request.POST['im_name']
		imm = Immunization.objects.get(immunizationid=int(imm_name))
		patient = Patient.objects.get(patientid=int(id_number))
		record = ImmunizationRecord(patient=patient,immunization=imm)
		if ImmunizationRecord.objects.filter(patient=patient, immunization=imm).exists():
			print "already there"
		else:
			record.save()
		redirecturl = "/patient/" + str(id_number)
		return HttpResponseRedirect(redirecturl)
	return HttpResponseRedirect("/")

def patientview(request, patientid):
	context = RequestContext(request)

	current_patient = Patient.objects.get(patientid=patientid)
	records = ImmunizationRecord.objects.filter(patient=current_patient)
	immunizations_needed = Immunization.objects.filter(recommended_age__lte=current_patient.age)
	list_needed = []
	#for im in immunizations_needed:
	#	x = records.get(immunization=im)
	#	if x.exists():
	#		im.delete()

	return render_to_response('dashboard/patient_view.html', {'current_patient': current_patient, 'records': records, 'needed': immunizations_needed}, context)

"""
curl -X POST --data-urlencode "code=l1pCK8wg2hoguI9SJyr0MCgzPG20dH&grant_type=authorization_code&redirect_uri=http%3A//0.0.0.0%3A5000/&client_id=Exc7zW1HfQNhC6bqqcDmrYtzVmH8IEF8QHLvcmQ4&client_secret=nblr5Gnj34y7eC8a2ZhiO0Gk29L0ZixNAPrYqAGkn1XEkmX8PY8dOtGcmmV68yO7TsckTPfV1OOVilEQPm8ztFSLYmEc5JuxuHRWDPheZ0vqlFl2HVvo7EjjR9hSZeaa" https://drchrono.com/o/token/
"""