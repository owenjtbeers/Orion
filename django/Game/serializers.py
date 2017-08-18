#Serializers.py

from rest_framework import serializers
from Game.models import Game

class GameSerializer(serializers.ModelSerializer):
	class Meta:
		model = Game

		fields = '__all__'