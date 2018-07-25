from django.urls import path
from rest_framework.routers import DefaultRouter

from explora.api.views import BlockData, get_blocks
router = DefaultRouter()

router.register('blocks', BlockData, base_name='blocks')

urlpatterns = [
    path('get-info/', get_blocks, name='get_blocks'),


]

urlpatterns += router.urls
