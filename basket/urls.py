from django.urls import include, path
from . import views


urlpatterns = [
    path('basket/', views.BasketAPIView.as_view({'get': 'list'}), name='basket'),
    path('addtobasket/', views.AddToBasketView.as_view(), name='add-to-basket'),
    path('removefrombasket/', views.RemoveFromBasketView.as_view(), name='remove-from-basket'),
    path('checkout/', views.CheckOutView.as_view(), name='remove-from-basket')
]