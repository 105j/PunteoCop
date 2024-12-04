from django.contrib import admin
from .models import area1, area2, area3, area4, area5
from .models import inventario1, inventario2, inventario3, inventario4, inventario5

# Personalización básica del área
class AreaAdmin(admin.ModelAdmin):
    list_display = ('sku', 'articulo')  # Campos a mostrar en la lista
    search_fields = ('sku', 'articulo')  # Campos para búsqueda
    list_filter = ('sku', 'articulo')  # Filtro lateral

# Registro de los modelos de área
admin.site.register(area1, AreaAdmin)
admin.site.register(area2, AreaAdmin)
admin.site.register(area3, AreaAdmin)
admin.site.register(area4, AreaAdmin)
admin.site.register(area5, AreaAdmin)

# Personalización básica del inventario
class InventarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'colaborador', 'fecha')  # Campos a mostrar en la lista
    search_fields = ('nombre', 'colaborador')  # Campos para búsqueda
    list_filter = ('fecha',)  # Filtro lateral
    filter_horizontal = ('sku',)  # Selector horizontal para relaciones ManyToMany

# Registro de los modelos de inventario
admin.site.register(inventario1, InventarioAdmin)
admin.site.register(inventario2, InventarioAdmin)
admin.site.register(inventario3, InventarioAdmin)
admin.site.register(inventario4, InventarioAdmin)
admin.site.register(inventario5, InventarioAdmin)