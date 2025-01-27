from urllib import response
from django.shortcuts import render 
from rest_framework.response import
from API.app.serializerrs import ContactSerializer
from rest_framework.views import APIView # type: ignore
from models import nameAPI


def index(APIvi):

    def grt(self,request):
        contacts=nameAPI.objects.all()
        serializer=ContactSerializer(contacts,many=True)
        return response(serializer.data)


