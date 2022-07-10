from rest_framework import serializers
from offers.models import userdetails

class userdetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = userdetails
        fields = '__all__'
