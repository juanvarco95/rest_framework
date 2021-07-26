from django.urls import path

from apps.products.api.views.general_views import MeasureUnitListAPIView, IndicadorAPIView, CategoryProductsListAPIView
from apps.products.api.views.product_views import ProductListAPIView

urlpatterns = [
    path('measure_unit/', MeasureUnitListAPIView.as_view(), name = 'measure_unit'),
    path('indicator/', IndicadorAPIView.as_view(), name = 'indicator'),
    path('category_products/', CategoryProductsListAPIView.as_view(), name = 'category_products'),
    path('product/', ProductListAPIView.as_view(), name = 'product')
]
