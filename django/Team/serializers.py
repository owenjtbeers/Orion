#Serializers.py

from rest_framework import serializers
from Team.models import Team, Roster
from Person.serializers import PlayerSerializer

def getPlayerName(roster, playerNo):

	if playerNo == 'captain':
		player = roster.captain
	else:
		player = getattr(roster, 'player'+str(playerNo))
	
	if player is None:
		return ''
	nameString = PlayerSerializer().getFirstName(player) + ' ' + PlayerSerializer().getLastName(player)
	return nameString

class TeamSerializer(serializers.ModelSerializer):
	class Meta:
		model = Team

		fields = '__all__'

class RosterNameSerializer(serializers.ModelSerializer):

	cap = serializers.SerializerMethodField('getcap')
	p1 = serializers.SerializerMethodField('getp1')
	p2 = serializers.SerializerMethodField('getp2')
	p3 = serializers.SerializerMethodField('getp3')
	p4 = serializers.SerializerMethodField('getp4')
	p5 = serializers.SerializerMethodField('getp5')
	p6 = serializers.SerializerMethodField('getp6')
	p7 = serializers.SerializerMethodField('getp7')
	p8 = serializers.SerializerMethodField('getp8')
	p9 = serializers.SerializerMethodField('getp9')

	def getcap(self, roster):
		return getPlayerName(roster, 'captain')

	def getp1(self, roster):
		return getPlayerName(roster, 1)

	def getp2(self, roster):
		return getPlayerName(roster, 2)

	def getp3(self, roster):
		return getPlayerName(roster, 3)

	def getp4(self, roster):
		return getPlayerName(roster, 4)

	def getp5(self, roster):
		return getPlayerName(roster, 5)

	def getp6(self, roster):
		return getPlayerName(roster, 6)

	def getp7(self, roster):
		return getPlayerName(roster, 7)

	def getp8(self, roster):
		return getPlayerName(roster, 8)

	def getp9(self, roster):
		return getPlayerName(roster, 9)

	class Meta:
		model = Roster
		fields = ('cap', 'p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9',)