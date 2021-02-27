from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.GamesView.as_view({'get': 'list'}), name='games'),
    path('categorized/', views.CategorizedGamesView.as_view({'get': 'list'}), name='categorized'),
    path('ownedgames/', views.OwnedGamesView.as_view({'get': 'list'}), name='owned-games'),
]