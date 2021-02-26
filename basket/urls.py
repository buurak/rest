from django.urls import include, path
from .views import BasketAPIView, AddToBasketView


urlpatterns = [
    path('basket/', BasketAPIView.as_view({'get': 'list'}), name='basket'),
    path('addtobasket/', AddToBasketView.as_view(), name='add-to-basket'),
]