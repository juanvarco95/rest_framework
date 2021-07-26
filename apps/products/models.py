
from django.db import models
from django.db.models.deletion import CASCADE
from django.forms.models import ModelChoiceField
from simple_history.models import HistoricalRecords
from apps.base.models import BaseModel

class MeasureUnit(BaseModel):

    description = models.CharField('Descripción', max_length = 50, blank = False, null = False, unique = True)
    historical = HistoricalRecords()
    
    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = "Unidad de medida"
        verbose_name_plural = "Unidades de medidas"

    def __str__(self):
        return self.description

class CategoryProduct(BaseModel):

    description = models.CharField('Descripción', max_length = 50, blank = False, null = False)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = "Categoria de Producto"
        verbose_name_plural = "Categorías de productos"

    def __str__(self):
        return self.description

class Indicador(BaseModel):

    descount_value = models.PositiveSmallIntegerField(default = 0, verbose_name = 'Indicador de Oferta')
    category_product = models.ForeignKey(CategoryProduct, on_delete = CASCADE, verbose_name = 'Categoría del Producto')  
    historical =  HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = "Indicador de Oferta"
        verbose_name_plural = "Indicadores de Ofertas"

    def __str__(self):
        return f'Oferta de la categoría {self.category_product} : {self.descount_value}%'

class Product(BaseModel):

    name = models.CharField('Nombre del Producto', max_length = 150, unique = True, blank = False, null = False)
    description = models.TextField('Descripción del producto', blank = False, null = False)
    image = models.ImageField('Imagen del Producto', upload_to = 'products/', blank = True, null = True)
    measure_unit = models.ForeignKey(MeasureUnit, on_delete = CASCADE, verbose_name = 'Unidad de Medida', null = True)
    category_product = models.ForeignKey(CategoryProduct, on_delete = CASCADE, verbose_name = 'Categoría del Producto', null = True)
    historical =  HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'


    def __str__(self):
        return self.name




  


