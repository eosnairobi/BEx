from rest_framework import serializers

from ..models import PriceListing


class PriceListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceListing
        fields = '__all__'
