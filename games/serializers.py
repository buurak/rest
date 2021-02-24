from .models import Game, Category
from rest_framework import serializers


class GameSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('url', 'name', 'year', 'category')

class CatSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('name', 'year', 'category')


