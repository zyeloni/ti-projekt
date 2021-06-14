from rest_framework.parsers import JSONParser
from .models import Players, EntityStats
from .serializers import PlayersSerializer, EntityStatsSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Count

@api_view(['GET', 'POST'])
def players_list(request):
    if request.method == 'GET':
        players = Players.objects.all()
        serializer = PlayersSerializer(players, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PlayersSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def entity_state(request,uid):
    if request.method == 'GET':
        res = EntityStats.objects.all().values('player', 'entityType').annotate(total = Count('entityType'))
        return Response(res)
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = EntityStatsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




