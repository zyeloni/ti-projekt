from django.db.models.functions import Coalesce, Lower
from rest_framework.parsers import JSONParser
from .models import Players, EntityStats, BlockStats, KillStats
from .serializers import PlayersSerializer, EntityStatsSerializer, BlockStatsSerializer, KillStatsSerializer
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
def entity_state(request, uid):
    if request.method == 'GET':
        res = EntityStats.objects.filter(player=uid).values('player', 'entityType').annotate(total = Count('entityType')).order_by('total').reverse()
        return Response(res)
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = EntityStatsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def all_entity_state(request):
    res = EntityStats.objects.values('player').annotate(total = Count('entityType'))
    return Response(res)

@api_view(['GET'])
def kill_stats(request):
    res = KillStats.objects.values('killer', 'victim')
    return Response(res)


@api_view(['GET', 'POST'])
def block_state(request, uid):
    if request.method == 'GET':
        res = BlockStats.objects.filter(player=uid).values('player').annotate(total = Count('blockType'))
        return Response(res)
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BlockStatsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def kill_state(request, uid, met):
    if request.method == 'GET':
        if met == 'killer':
            res = KillStats.objects.filter(killer=uid).all()
        elif met == 'victim':
            res = KillStats.objects.filter(victim=uid).all()
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = KillStatsSerializer(res, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def add_kill(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = KillStatsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def last_kill(request):
    if request.method == 'GET':
        res = KillStats.objects.all().order_by('createdAt').reverse()[:10]
        serializer = KillStatsSerializer(res, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)




