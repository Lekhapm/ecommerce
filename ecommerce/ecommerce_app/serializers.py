from rest_framework import serializers
from .models import Store,Category,Subcategory,Product,StoreProduct
class StoreSerializer(serializers.ModelSerializer):
	class Meta:
		model = Store
		# fields = List of Fields
		fields='__all__'
class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		# fields = List of Fields
		fields='__all__'
class SubCategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Subcategory
		# fields = List of Fields
		fields='__all__'
class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		# fields = List of Fields
		fields='__all__'
class StoreProductserializer(serializers.ModelSerializer):
	class Meta:
		model = StoreProduct
		# fields = List of Fields
		fields='__all__'