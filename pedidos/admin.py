from django.contrib import admin

from .models import Pedido, Linea_pedido
# Register your models here.
class PedidoAdmin(admin.ModelAdmin):
    readonly_fields=(['created_at'])

class LineaPedidoAdmin(admin.ModelAdmin):
    readonly_fields=(['created_at'])   


admin.site.register(Pedido, PedidoAdmin)

admin.site.register(Linea_pedido, LineaPedidoAdmin)
