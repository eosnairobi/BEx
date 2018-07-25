from django.urls import path, re_path
from .api.views import PriceListingViewSet, prices 
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'api/pricing', PriceListingViewSet, base_name='pricing')

urlpatterns = [
    path('prices/', prices, name='prices'),
]

urlpatterns+=router.urls