#deletionScript

from django.core.management.base import BaseCommand, CommandError

from django.db import transaction
from League.models import League
from Person.models import Person, Referee, Player
from Game.models import Game
from Team.models import Team, Roster

class Command(BaseCommand):

    @transaction.atomic
    def handle(self, *args, **options):
        League.objects.all().delete()
        Team.objects.all().delete()
        Person.objects.all().delete()
        Game.objects.all().delete()