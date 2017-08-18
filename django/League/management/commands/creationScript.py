from django.core.management.base import BaseCommand, CommandError

from django.db import transaction
from League.models import League
from Person.models import Person, Referee, Player
from Game.models import Game
from Team.models import Team, Roster

from datetime import datetime, timedelta

class Command(BaseCommand):

	@transaction.atomic
	def handle(self, *args, **options):

		startDate = datetime(year=2017, month=3, day=1)
		endDate = startDate + timedelta(days=56)
		registrationDate = startDate - timedelta(days=7)
		
		#Create League
		league1, _ = League.objects.get_or_create(name="La Ligue 1", startDate=startDate, endDate = endDate,
												 registrationDeadline=registrationDate, active=True, day='M')
		league2, _ = League.objects.get_or_create(name="Extraordinary Gentlemen", startDate=startDate, endDate = endDate,
												 registrationDeadline=registrationDate, active=False, day='T')

		#Create some ppl, cause we need them for teh party
		person1, _ = Person.objects.get_or_create(first="Jowen", last="Speers")
		person2, _ = Person.objects.get_or_create(first="Harvis", last="Akazamzarak")
		person3, _ = Person.objects.get_or_create(first="Bliss", last="Percocette")

		player1, _ = Player.objects.get_or_create(person=person1)
		player2, _ = Player.objects.get_or_create(person=person2)
		referee1, _ = Referee.objects.get_or_create(person=person3)

		roster1, _ = Roster.objects.get_or_create(captain=player1)
		roster2, _ = Roster.objects.get_or_create(captain=player2)

		team1, _ = Team.objects.get_or_create(league=league1, roster=roster1, name="Shark Attack")
		team2, _ = Team.objects.get_or_create(league=league1, roster=roster2, name="Needs a bigger boat")

		gameTIME = datetime(year=2017, month=3, day=1, hour=7)
		game = Game.objects.get_or_create(league=league1, homeTeam=team1, awayTeam=team2,
										  time=gameTIME)






