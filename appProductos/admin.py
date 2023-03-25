from django.contrib import admin
from .models import *
# Register your models here.
#----------------------------------
class categoriaAdmin(admin.ModelAdmin):
    list_display = ['id','descripCategoria']

admin.site.register(categoria, categoriaAdmin)

#----------------------------------------
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre','descripcion','existencia']

admin.site.register(producto, ProductoAdmin)

#---------------------------------------
# class CarroAdmin(admin.ModelAdmin):
#     list_display = ['usuario','productos','cantidad','estado']

# admin.site.register(carro, CarroAdmin)
