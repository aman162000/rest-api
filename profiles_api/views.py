from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import HelloSerializer
from django.shortcuts import Http404
# Create your views here.

class HelloApiView(APIView):

    serializer_class = HelloSerializer

    def get(self,request,format = None):
        an_apiview = ['A','B','C','D','E','F','G',]

        return Response({'message':'Hello','an_apiview':an_apiview})

    def post(self,request,format = None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors,
                            status = status.HTTP_400_BAD_REQUEST
                            )

    def put(self,request,pk=None):
             return Response({'method':'PUT'})

    def patch(self,request,pk=None):
        return Response({'method':'patch'})

    def delete(self,request,pk=None):
        return Response({'method':'Delete'})