from django.contrib import admin
from .models import Store
from .models import Category,Subcategory,Product,StoreProduct,Customer,StoreAdmin,Cart,CartItem

# Register your models here.
admin.site.register(Store)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Product)
admin.site.register(StoreProduct)
admin.site.register(Customer)
admin.site.register(StoreAdmin)
admin.site.register(Cart)
admin.site.register(CartItem)


