# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from League.serializers import LeagueSerializer
from League.models import League
# Create your views here.

#
class LeagueView(APIView):
    
    @csrf_exempt
    def get(self, request, format=None):
            
        if 'active' in request.GET:
            if request.GET['active'].lower()=='true':
                leagues = League.objects.filter(active=True)
            elif request.GET['active'].lower()=='false':
                leagues = League.objects.filter(active=False)
            else:
                return HttpResponse(status=400)
        else:
            leagues = League.objects.all()
        serializer = LeagueSerializer(leagues, many = True)

        return Response(serializer.data, status=200)