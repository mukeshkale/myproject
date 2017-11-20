# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from .models import Person
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

#def index(request):
#    output = Person.objects.all()
#    template = loader.get_template('blog/index.html')
#    context = {
#        'output': output,
#    }
#    return HttpResponse(template.render(context, request))
    #latest_person_list = Person.objects.order_by('person_firstname')[:5]
    #output = ', '.join([q.person_firstname for q in latest_person_list])
 #   html = ''
  #  for i in output:
   #     url = '/blog/' + str(i.id) + '/'
    #    html += '<a href="' + url + '">' + i.person_firstname + '</a> <br>'
    #return HttpResponse(html)

#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")

def base():
    base = loader.get_template(blog/base.html)
    return HttpResponse(base)

#def detail(request, person_id):
#    return HttpResponse("You're looking at person %s." % person_id)

def detail(request, person_id):
    opdetails = get_object_or_404(Person, pk=person_id)
    return render(request, 'blog/details.html', {'opdetails': opdetails })




def index(request):
    p_list = Person.objects.all()
    paginator = Paginator(p_list, 3)
    page = request.GET.get('page')
    try:
        d_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        d_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        d_list = paginator.page(paginator.num_pages)

    return render(request, 'blog/index.html', {'d_list': d_list})