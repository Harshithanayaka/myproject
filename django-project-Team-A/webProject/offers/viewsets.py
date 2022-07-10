from rest_framework import viewsets

from offers import serializers
from offers.models import userdetails

class UserdetailsViewSet(viewsets.ModelViewSet):
    queryset = userdetails.objects.all()
    serializer_class = serializers.userdetailsSerializer

