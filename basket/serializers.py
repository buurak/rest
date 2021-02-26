from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Basket, BasketItem
from games.models import Game
from games.serializers import CategorizedSearchSerializer


class BasketItemSerializer(serializers.Serializer):
    game = CategorizedSearchSerializer(many=True, read_only=True)
    name = serializers.CharField()
    year = serializers.IntegerField()
    category = serializers.CharField()

    class Meta:
        model = BasketItem
        fields = ('basket', 'game')


class BasketSerializer(serializers.ModelSerializer):
    games = BasketItemSerializer(many=True)

    class Meta:
        model = Basket
        fields = ('user','games')
