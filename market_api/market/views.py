from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import OziqOvqatSerializer
from .models import OziqOvqat


class OziqlistApiView(APIView):
    def get(self,request):
        articles=OziqOvqat.objects.all()
        serializers=OziqOvqatSerializer(articles,many=True).data
        data={
            "status":True,
            "message":"Barcha Oziq Ovqtlar",
            "articles":serializers
        }
        return Response(data)












