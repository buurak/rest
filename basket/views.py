from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from django.db.models import Q

from .models import Basket, BasketItem
from games.models import Game
from .serializers import BasketSerializer, BasketItemSerializer
from users.serializers import UserSerializer

from django.contrib.auth.models import User


class BasketAPIView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self, request):
        username = self.request.GET.get('username')
        user_info = User.objects.filter(username=username)
        user_id = user_info[0].id
        queryset = Basket.objects.filter(user=user_id)
        return queryset

    def list(self, request, *args, **kwargs):
        serializer = BasketSerializer(self.get_queryset(request), many=True)
        return Response(serializer.data)

    def add_to_basket(self, request):
        game_name = self.request.GET.get('name')
        username = self.request.GET.get('username')
        user = User.objects.get(username=username)
        game = Game.objects.get(name=game_name)

        try:
            basket = Basket.get_object_or_404(Q(user__username__icontains=username))
            basket_item = BasketItem(game=game, basket=basket)
            basket_item.save()
            
        except:
            basket = Basket(user=user)
            basket.save()
            basket_item = BasketItem(game=game, basket=basket)
            basket_item.save()

