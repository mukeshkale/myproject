# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Person

def index(request):
    latest_person_list = Person.objects.order_by('person_firstname')[:5]
    output = ', '.join([q.person_firstname for q in latest_person_list])
    return HttpResponse(output)

#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, person_id):
    return HttpResponse("You're looking at question %s." % person_id)
