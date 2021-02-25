from django.urls import include, path
# from rest_framework import routers
from .views import BasketAPIView

# router = routers.DefaultRouter()
# router.register(r'store', views.BasketAPIView)


urlpatterns = [
    path('basket/', BasketAPIView.as_view({'get': 'list'}), name='basket'),
]