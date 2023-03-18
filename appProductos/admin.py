from django.contrib import admin
from .models import *
# Register your models here.
#----------------------------------
class categoriaAdmin(admin.ModelAdmin):
    list_display = ['id','descripCategoria']

admin.site.register(categoria, categoriaAdmin)

#----------------------------------------


admin.site.register(producto, productoAdmin)
admin.site.register(carro, carroAdmin)
