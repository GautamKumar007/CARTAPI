from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests

from .models import Cart
from .mycart import cartSerializer

# Create your views here.

def index(request):
    return HttpResponse('<h1>Wellcome to Cart Api</h1>')

class cartList(APIView):
    
    def get(self, request):
        item = Cart.objects.all()
        serializer = cartSerializer(item, many=True)
        return Response(serializer.data)


    def post(self, request):
        seril = cartSerializer(data=request.data)
        if seril.is_valid():
            seril.save()
            return Response(seril.data, status=status.HTTP_201_CREATED)
        return Response(seril.errors, status=status.HTTP_400_BAD_REQUEST)



class cartDetail(APIView):

    def get_item(self, pk):
        try:
            return Cart.objects.get(prod_id=pk)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        item = self.get_item(pk)
        serializer = cartSerializer(item)
        return Response(serializer.data)


    def put(self, request, pk, format=None):
        item = self.get_item(pk)
        serializer = cartSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        item = self.get_item(pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class cartLength(APIView):
    def get(self, request):
        cart_length = len(Cart.objects.all())
        return Response(cart_length)


class idList(APIView):
    def get(self, request):
        url="http://127.0.0.1:8000/viewcart/"
        r = requests.get(url).json()
        len=[]
        for ids in r:
            prod_id = ids['prod_id']
            len.append(prod_id)

        return Response(len)