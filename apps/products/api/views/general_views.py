from rest_framework import viewsets

from apps.base.api import GeneralListApiView
from apps.products.api.serializers.general_serializers import MeasureUnitSerializer, IndicadorSerializer, CategoryProductSerializer

class MeasureUnitViewSet(viewsets.ModelViewSet):
    serializer_class = MeasureUnitSerializer
  

class CategoryProductsViewSet(viewsets.ModelViewSet):
    serializer_class = CategoryProductSerializer


class IndicadorViewSet(viewsets.ModelViewSet):
    serializer_class = IndicadorSerializer

    

