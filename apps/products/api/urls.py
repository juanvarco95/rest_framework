from django.urls import path

from apps.products.api.views.general_views import MeasureUnitListAPIView, IndicadorAPIView, CategoryProductsListAPIView
from apps.products.api.views.product_views import ProductListCreateAPIView, ProductRetrieveUpdateDestroyAPIView
urlpatterns = [
    path('measure_unit/', MeasureUnitListAPIView.as_view(), name = 'measure_unit'),
    path('indicator/', IndicadorAPIView.as_view(), name = 'indicator'),
    
]
