from .models import Game, OwnedGames
from rest_framework import serializers


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'name', 'year', 'category')

        extra_kwargs = {
            "id": {'required': False},
        }


class OwnedGameSerializer(serializers.ModelSerializer):
    games = GameSerializer(many=True)

    class Meta:
        model = OwnedGames
        fields = ('user','games')
