from django.db import models
from apps.products.models import MeasureUnit, CateroryProduct, Indicador

from rest_framework import serializers

class MeasureUnitSerializer(serializers.ModelSerializer):

    class Meta:
        model = MeasureUnit
        exclude = ('state',)

class CategoryProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = CateroryProduct
        exclude = ('state',)

class IndicadorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Indicador
        exclude = ('state', )
