from django.urls import path
from rest_framework.routers import DefaultRouter

from .api.views import BlockData
router = DefaultRouter()

router.register('blocks', BlockData, base_name='blocks')

urlpatterns = [
    


]

urlpatterns += router.urls