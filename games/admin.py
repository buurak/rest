from django.contrib import admin
from .models import Game, Category, OwnedGames


admin.site.register(Game)
admin.site.register(Category)
admin.site.register(OwnedGames)