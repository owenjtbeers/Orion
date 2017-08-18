# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from Team.models import Team
from Person.models import Referee
from League.models import League
# Create your models here.

class Game(models.Model):
	league = models.ForeignKey(League, blank=False, null=False)
	homeTeam = models.ForeignKey(Team, related_name='homeTeam', blank=False, null=False)
	awayTeam = models.ForeignKey(Team, related_name='awayTeam', blank=False, null=False)
	referee = models.ForeignKey(Referee, blank=True, null=True)
	time = models.DateTimeField(null=False, blank=False)
	homeScore = models.IntegerField(null=True, blank=True)
	awayScore = models.IntegerField(null=True, blank=True)
	gameNumber = models.IntegerField(null=True, blank=True)

	def __str__(self):
		return "Home: {} vs. Away: {} @ {}".format(self.homeTeam.name, self.awayTeam.name,
												   time.strftime("%B %d %H:%M"))

