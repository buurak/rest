from .models import Game, Category
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import filters
from games.serializers import GameSearchSerializer, CatSearchSerializer
from rest_framework import request
from django.db.models import Q
from rest_framework.response import Response



class GamesView(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSearchSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    # permission_classes = [permissions.IsAuthenticated]

class CategorizedGamesView(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = CatSearchSerializer

    def get_queryset(self):
        filter_ = self.request.GET.get('filter')
        search = self.request.GET.get('search')
        queryset = Game.objects.filter(category__name=filter_)
        if search:
            queryset = queryset.filter(Q(name__icontains=search))
        return queryset

    def list(self, request, *args, **kwargs):
        serializer = CatSearchSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)
