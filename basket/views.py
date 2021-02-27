from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from django.db.models import Q
from rest_framework.views import APIView

from .models import Basket, BasketItem
from games.models import Game, OwnedGames
from .serializers import BasketSerializer, BasketItemSerializer
from games.serializers import GameSerializer

from django.contrib.auth.models import User


class BasketAPIView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = Basket.objects.filter(user=user.id)
        return queryset

    def list(self, request, *args, **kwargs):
        serializer = BasketSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)


class AddToBasketView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        game_id = self.request.GET.get('game_id')
        user = self.request.user
        game = Game.objects.get(id=game_id)

        try:
            basket = Basket.objects.get(user=user)
            basket_item = BasketItem.objects.create(game=game, basket=basket)  
        except:
            basket = Basket.objects.create(user=user)
            basket_item = BasketItem.objects.create(game=game, basket=basket)

        return Response({'ok':True}, 200)


class RemoveFromBasketView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        game_id = self.request.GET.get('game_id')
        user = self.request.user
        game = Game.objects.get(id=game_id)
        basket = Basket.objects.get(user=user)
        basket_item = BasketItem.objects.filter(game=game, basket=basket).first().delete()

        return Response({'ok':True}, 200)


class CheckOutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        permission_classes = [permissions.IsAuthenticated]
        user = self.request.user
        basket_id = self.request.GET.get('basket_id')
        basket = Basket.objects.get(id=basket_id)
        basket_items = basket.basket_item.all()
        owned_games, created = OwnedGames.objects.get_or_create(user=user)
        for basket_item in basket_items:
            game = basket_item.game.id
            owned_games.games.add(game)
        owned_games.save()
        basket.delete()
        
        return Response({'ok':True}, 200)
        
        