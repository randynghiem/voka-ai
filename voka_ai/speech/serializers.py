from rest_framework import serializers
from .models import RequestItem

class RequestItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RequestItem
        fields = ['user_email', 'link', 'text', 'date']