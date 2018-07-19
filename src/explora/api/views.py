import json

import requests

from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..models import Block
from .serializers import BlockSerializer

API_URL = 'http://api.eosargentina.io/v1/chain/get_block'


@api_view
def get_block_data(block_num_or_id):
    r = requests.post(API_URL, data=json.dumps(
        {'block_num_or_id': block_num_or_id}), verify=False)
    print(r.text)
    return Response(r.text)


class BlockData(viewsets.ReadOnlyModelViewSet):
    queryset = Block.objects.all()
    serializer_class = BlockSerializer
