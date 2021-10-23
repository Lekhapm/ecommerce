from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Store(models.Model):
	name=models.CharField(max_length=30)
	address=models.CharField(max_length=30)
	phone=models.CharField(max_length=30)
	def __str__(self):
		return self.name
class Category(models.Model):
	name=models.CharField(max_length=30)
	description=models.CharField(max_length=30)
	
	def __str__(self):
		return self.name

class Subcategory(models.Model):
	category=models.ForeignKey(Category, on_delete=models.CASCADE)
	name=models.CharField(max_length=30)
	description=models.CharField(max_length=30)
	
	def __str__(self):
		return self.name

class Product(models.Model):
	subcategory=models.ForeignKey(Subcategory, on_delete=models.CASCADE)
	name=models.CharField(max_length=30)
	description=models.CharField(max_length=30)
	price=models.DecimalField(max_digits=5, decimal_places=2)
	def __str__(self):
		return self.name
class StoreProduct(models.Model):
	store=models.ForeignKey(Store, on_delete=models.CASCADE)
	product=models.ForeignKey(Product, on_delete=models.CASCADE)
	stock=models.IntegerField()
	
	def __str__(self):
		return self.product.name
class Customer(models.Model):
	user=models.OneToOneField(User, on_delete=models.CASCADE)
	phone=models.CharField(max_length=30,null=True)
	adress=models.CharField(max_length=30,null=True)

	def __str__(self):
		return self.user.username
class StoreAdmin(models.Model):
	user=models.OneToOneField(User, on_delete=models.CASCADE)
	adress=models.CharField(max_length=30,null=True)
	def __str__(self):
		return self.user.username
class Cart(models.Model):
	name=models.CharField(max_length=30,null=True)
	user=models.ForeignKey(Customer, on_delete=models.CASCADE)
	def __str__(self):
		return self.name
class CartItem(models.Model):
	cart=models.ForeignKey(Cart, on_delete=models.CASCADE)
	product=models.ForeignKey(Product, on_delete=models.CASCADE)
	quantity=models.IntegerField(null=True)
	price=models.IntegerField(null=True)
	active_status=models.BooleanField(default=False)
	def __str__(self):
		return self.cart.name