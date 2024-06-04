from django.contrib import admin
from .models import Product, Customer

# Register your models here.
@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display=['id','titulo','autor','fuente','categoria','imagen_producto']
    
@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','usuario','nombre','fecha','bitacora']