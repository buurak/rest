from .models import Game, OwnedGames
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import filters
from rest_framework.response import Response
from games.serializers import GameSerializer, OwnedGameSerializer
from rest_framework import request
from django.db.models import Q
from django.contrib.auth.models import User


class GamesView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class CategorizedGamesView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    def get_queryset(self):
        filter_ = self.request.GET.get('filter')
        search = self.request.GET.get('search')
        queryset = Game.objects.filter(category__name=filter_)
        if search:
            queryset = queryset.filter(Q(name__icontains=search))
        return queryset

    def list(self, request, *args, **kwargs):
        serializer = GameSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)
        

class OwnedGamesView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = OwnedGames.objects.all()
    serializer_class = OwnedGameSerializer

    def get_queryset(self):
        queryset = OwnedGames.objects.filter(user=self.request.user)
        return queryset

    def list(self, request, *args, **kwargs):
        serializer = OwnedGameSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)