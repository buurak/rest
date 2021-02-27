from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Basket, BasketItem
from games.models import Game
from games.serializers import GameSerializer


class BasketItemSerializer(serializers.Serializer):
    name = serializers.CharField()
    year = serializers.IntegerField()
    category = serializers.CharField()

    class Meta:
        model = BasketItem
        fields = ('id', 'basket', 'game')


class BasketSerializer(serializers.ModelSerializer):
    games = BasketItemSerializer(many=True)
    # games = serializers.RelatedField(source='game', read_only=True)

    class Meta:
        model = Basket
        fields = ['user','games']


