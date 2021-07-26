from apps.base.api import GeneralListApiView
from apps.products.api.serializers.general_serializers import MeasureUnitSerializer, IndicadorSerializer, CategoryProductSerializer

class MeasureUnitListAPIView(GeneralListApiView):
    serializer_class = MeasureUnitSerializer
  

class CategoryProductsListAPIView(GeneralListApiView):
    serializer_class = CategoryProductSerializer


class IndicadorAPIView(GeneralListApiView):
    serializer_class = IndicadorSerializer

    

