from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from dashboard.models import Patient, Immunization, ImmunizationRecord
import json as simplejson

def home(request):
    context = RequestContext(request)
    return render_to_response('dashboard/home.html', {}, context)
# Create your views here.
