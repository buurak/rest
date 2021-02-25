from .models import Game
from rest_framework import serializers


class GameSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('url', 'name', 'year', 'category')

class CategorizedSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('name', 'year', 'category')
