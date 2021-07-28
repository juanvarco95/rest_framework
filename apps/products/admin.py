from django.contrib import admin
from apps.products.models import *

class MeasureUnitAdmin(admin.ModelAdmin):
    list_display = ('description',)

admin.site.register(MeasureUnit, MeasureUnitAdmin)
admin.site.register(CategoryProduct)
admin.site.register(Indicador)
admin.site.register(Product)
