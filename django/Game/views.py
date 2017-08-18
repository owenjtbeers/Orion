# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from Game.serializers import GameSerializer
from Game.models import Game
# Create your views here.

#
class GameView(APIView):
	
    @csrf_exempt
    def get(self, request, format=None):

        if 'league_id' in request.GET:
            games = Game.objects.filter(league__id=request.GET['league_id'])
        else:
            return HttpResponse(status=400)

        serializer = GameSerializer(games, many=True)

        return Response(serializer.data, status=200)