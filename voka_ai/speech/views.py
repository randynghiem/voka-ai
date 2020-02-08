from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from speech.models import RequestItem
from speech.serializers import RequestItemSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class RequestItemList(APIView):
    """
    List all request items or create a new request item
    """
    def get(self, request, format=None):
        items = RequestItem.objects.all()
        serializer = RequestItemSerializer(items, many=True)
        return Response(serializer.data)