from django.contrib.auth.models import User
from .models import Game, Category
from rest_framework import serializers


class GameSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('url', 'name', 'year', 'category')


