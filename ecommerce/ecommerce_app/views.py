from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from .models import Store,Category,Subcategory,Product,StoreProduct
from .serializers import StoreSerializer,CategorySerializer,SubCategorySerializer,ProductSerializer,StoreProductserializer
# Create your views here.
class Storelist(APIView):
	def get(self,request):
		stores=Store.objects.all()
		print("stores:",stores)
		serializer=StoreSerializer(stores,many=True)
		return Response(serializer.data)
class Categorylist(APIView):
	def get(self,request):
		category=Category.objects.all()
		print("category:",category)
		serializer=CategorySerializer(category,many=True)
		return Response(serializer.data)
class Subcategorylist(APIView):
	def get(self,request):
		subcategory=Subcategory.objects.all()
		print("subcategory:",subcategory)
		serializer=SubCategorySerializer(subcategory,many=True)
		return Response(serializer.data)
class Productlist(APIView):
	def get(self,request):
		product=Product.objects.all()
		print("product:",product)
		serializer=ProductSerializer(product,many=True)
		return Response(serializer.data)
class Storeproductlist(APIView):
	def get(self,request):
		store_product=StoreProduct.objects.all()
		print("product:",store_product)
		serializer=StoreProductserializer(store_product,many=True)
		return Response(serializer.data)


