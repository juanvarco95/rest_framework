from rest_framework import serializers

from apps.products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    measure_unit = serializers.StringRelatedField()
    category_product = serializers.StringRelatedField()

    class Meta:
        model = Product
        exclude = ('state', 'create_date', 'modified_date', 'deleted_date')