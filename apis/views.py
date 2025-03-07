from django.shortcuts import render
from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from .agent import *


class Getquery(APIView) :
    def post(self , request ) :
        data = request.data
        query = data['data']
        founder = Founder(query)
        result = founder.Processdata()
        return Response({
            "data" : result
        } , status=status.HTTP_200_OK)


