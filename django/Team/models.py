# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from League.models import League
from Person.models import Player
# Create your models here.

class Roster(models.Model):

	captain = models.ForeignKey(Player, related_name='captain', blank=False, null=False)
	player1 = models.ForeignKey(Player, related_name='player1', blank=True, null=True)
	player2 = models.ForeignKey(Player, related_name='player2', blank=True, null=True)
	player3 = models.ForeignKey(Player, related_name='player3', blank=True, null=True)
	player4 = models.ForeignKey(Player, related_name='player4', blank=True, null=True)
	player5 = models.ForeignKey(Player, related_name='player5', blank=True, null=True)
	player6 = models.ForeignKey(Player, related_name='player6', blank=True, null=True)
	player7 = models.ForeignKey(Player, related_name='player7', blank=True, null=True)
	player8 = models.ForeignKey(Player, related_name='player8', blank=True, null=True)
	player9 = models.ForeignKey(Player, related_name='player9', blank=True, null=True)

	def __str__(self):
		return self.captain.first + ' ' + self.captain.last

class Team(models.Model):

	league = models.ForeignKey(League, blank=False, null=False)
	roster = models.ForeignKey(Roster, blank=False, null=False)
	name = models.CharField(max_length=50, null=False, blank=False)

	def __str__(self):
		return self.name
