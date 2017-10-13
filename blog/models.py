# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Person(models.Model):
    person_firstname = models.CharField(max_length=50)
    person_lastname = models.CharField(max_length=50)
    person_city = models.CharField(max_length=50)
    person_age = models.IntegerField(default=0)

    def __str__(self):
        return self.person_firstname
