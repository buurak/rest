from django.contrib.auth.models import User
from .models import Game, Category
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import filters
from games.serializers import GameSearchSerializer



class GamesView(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSearchSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    # permission_classes = [permissions.IsAuthenticated]

