from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..models import PriceListing
from .serializers import PriceListingSerializer


class PriceListingViewSet(viewsets.ModelViewSet):
    serializer_class = PriceListingSerializer
    queryset = PriceListing.objects.all()

@api_view(['GET'])
def prices(request):
    data = []
    objects = PriceListing.objects.filter(currency__cmc_id=1765)
    for obj in objects:
        data.append([obj.time.timestamp(), obj.usd])
    return Response(data)