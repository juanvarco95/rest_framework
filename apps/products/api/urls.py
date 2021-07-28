from django.urls import path

from apps.products.api.views.general_views import MeasureUnitListAPIView, IndicadorAPIView, CategoryProductsListAPIView
from apps.products.api.views.product_views import ProductListCreateAPIView, ProductRetrieveAPIView, ProductDestroyAPIView, ProductUpdateAPIView

urlpatterns = [
    path('measure_unit/', MeasureUnitListAPIView.as_view(), name = 'measure_unit'),
    path('indicator/', IndicadorAPIView.as_view(), name = 'indicator'),
    path('category_products/', CategoryProductsListAPIView.as_view(), name = 'category_products'),
    path('product/', ProductListCreateAPIView.as_view(), name = 'product_create'),
    path('product/retrieve/<int:pk>', ProductRetrieveAPIView.as_view(), name = 'product_retrieve'),
    path('product/destroy/<int:pk>', ProductDestroyAPIView.as_view(), name = 'product_destroy'),
    path('product/update/<int:pk>', ProductUpdateAPIView.as_view(), name = 'product_update'),
    
]
