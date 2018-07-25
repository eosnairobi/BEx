from celery import shared_task
import requests
import json
from .models import Block
from django.db.models import Max

API_URL = 'http://api2.eosnairobi.io:8898/v1/chain/get_info'


@shared_task
def get_info():
    try:
        r = requests.get(API_URL, verify=False)
        data = json.loads(r.text)
        lib_num = data.get('last_irreversible_block_num')
        lib_id = data.get('last_irreversible_block_id')


        save_blocks(lib_num, lib_id)

    except Exception:
        pass


def save_blocks(lib=None, lib_id=None):
    # Get the last irreversible block and save from that to last lib
    try:
        last_lib = Block.objects.latest('block_num').block_num
        # last_lib = Block.objects.all().aggregate(Max('block_num'))['block__max']
    except Exception as e:
        # Create Block
        last_lib = 0

    while lib > last_lib:
            print(lib)
            Block.objects.create(block_num = lib, block_id=lib_id)
            lib -= 1


