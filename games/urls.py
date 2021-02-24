from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'games', views.GamesView)


urlpatterns = [
    path('', include(router.urls)),
    path('categorized/', views.CategorizedGamesView.as_view({'get': 'list'}), name='categorized')
]