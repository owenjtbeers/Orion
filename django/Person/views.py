# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from Person.serializers import PersonSerializer, PlayerSerializer
from Person.models import Person, Player
# Create your views here.

#
class PersonView(APIView):
	
	@csrf_exempt
	def get(self, request, format=None):
		if 'team_id' in request.GET:
			persons = Person.objects.filter(id=request.GET['team_id'])
		else:
			persons = Person.objects.all()

		serializer = PersonSerializer(persons, many=True)

		return Response(serializer.data, status=200)


class PlayerView(APIView):

	def get(self, request, format=None):

		players = Player.objects.all()

		serializer = PlayerSerializer(players, many=True)

		return Response(serializer.data, status=200)