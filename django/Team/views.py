# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from Team.serializers import TeamSerializer, RosterNameSerializer
from Team.models import Team, Roster

class TeamView(APIView):
    
    def get(self, request, format=None):
        
        if 'league_id' in request.GET:
            teams = Team.objects.filter(league__id=request.GET['league_id'])
        else:
            return HttpResponse(status=400)
        serializer = TeamSerializer(teams, many = True)

        return Response(serializer.data, status=200)

class RosterNamesView(APIView):

    def get(self, request, format=None):

        if 'team_id' in request.GET:
            rosters = Roster.objects.filter(team__id=request.GET['team_id'])

        else:
            return HttpResponse(status=400)

        serializer = RosterNameSerializer(rosters, many=True)

        return Response(serializer.data, status=200)
