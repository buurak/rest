from django.db import models
from django.conf import settings
from games.models import Game
from django.contrib.auth.models import User


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_info')
    games = models.ManyToManyField(Game, through='BasketItem')

    def __str__(self):
        return self.user.username

class BasketItem(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        return self.game.name