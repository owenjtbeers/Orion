#Serializers.py

from rest_framework import serializers
from Person.models import Person, Player

class PersonSerializer(serializers.ModelSerializer):
	class Meta:
		model = Person

		fields = '__all__'

class PlayerSerializer(serializers.ModelSerializer):

	first = serializers.SerializerMethodField('getFirstName')
	last = serializers.SerializerMethodField('getLastName')

	def getFirstName(self, player):

		if player is None:
			return None

		return player.person.first

	def getLastName(self, player):
		
		if player is None:
			return None
			
		return player.person.last
	
	class Meta:
		model = Player

		fields = ['first', 'last']