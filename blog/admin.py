# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Person

# class PostModelAdmin(admin.ModelAdmin):
#	list_display = ["__unicode__","timestamp"]
#	class Meta:
#		model = Post

# Register your models here.
admin.site.register(Person)
