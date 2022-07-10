from rest_framework import routers
from offers.models import userdetails

from offers.viewsets import UserdetailsViewSet

router = routers.DefaultRouter()
router.register('userdetails',UserdetailsViewSet)
