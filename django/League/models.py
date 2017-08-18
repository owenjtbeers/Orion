# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class League(models.Model):

	MON = 'M'
	TUE = 'T'
	WED = 'W'
	THU = 'R'
	FRI = 'F'
	SAT = 'S'
	SUN = 'U'

	DAY_CHOICES = (
		(MON, 'Monday'),
		(TUE, 'Tuesday'),
		(WED, 'Wednesday'),
		(THU, 'Thurdsday'),
		(FRI, 'Friday'),
		(SAT, 'Saturday'),
		(SUN, 'Sunday'),
	)
	
	name = models.CharField(max_length=100, blank=False, null=False)
	startDate = models.DateTimeField(null=False, blank=False)
	endDate = models.DateTimeField(null=False, blank=False)
	registrationDeadline = models.DateTimeField(null=False, blank=False)
	maxTeams = models.IntegerField(default=8)
	active = models.BooleanField(default=False)
	day = models.CharField(max_length=1, choices=DAY_CHOICES, default=SUN)

	def __str__(self):
		return self.name
# Create your models here.
