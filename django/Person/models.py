# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Person(models.Model):

	first = models.CharField(max_length=50, null=False, blank=False)
	last = models.CharField(max_length=50, null=False, blank=False)
	email = models.CharField(max_length=100, null=True, blank=True)
	address = models.CharField(max_length=100, null=True, blank=True)
	phone = models.CharField(max_length=20, null=True, blank=True)

	# This part is for the emergency contact
	emergencyContact = models.CharField(max_length=100, null=True, blank=True)
	emergencyPhone = models.CharField(max_length=20, null=True, blank=True)

	def __str__(self):
		return first + ' ' + last

class Referee(models.Model):
	person = models.ForeignKey(Person, related_name='referee')

	def __str__(self):
		return "Referee: {} {}".format(self.person.first, self.person.last)

class Player(models.Model):
	person = models.ForeignKey(Person, related_name='player')

	def __str__(self):
		return "Player: {} {}".format(self.person.first, self.person.last)

