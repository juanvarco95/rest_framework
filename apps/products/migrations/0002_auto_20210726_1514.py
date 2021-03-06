# Generated by Django 3.2.5 on 2021-07-26 20:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryProduct',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Fecha de Modificación')),
                ('delete_date', models.DateField(auto_now=True, verbose_name='Fecha de Eliminación')),
                ('description', models.CharField(max_length=50, verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Categoria de Producto',
                'verbose_name_plural': 'Categorías de productos',
            },
        ),
        migrations.CreateModel(
            name='HistoricalCategoryProduct',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Creación')),
                ('modified_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Modificación')),
                ('delete_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Eliminación')),
                ('description', models.CharField(max_length=50, verbose_name='Descripción')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Categoria de Producto',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.RemoveField(
            model_name='cateroryproduct',
            name='measure_unit',
        ),
        migrations.AddField(
            model_name='historicalproduct',
            name='measure_unit',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='products.measureunit', verbose_name='Unidad de Medida'),
        ),
        migrations.AddField(
            model_name='product',
            name='measure_unit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.measureunit', verbose_name='Unidad de Medida'),
        ),
        migrations.AlterField(
            model_name='historicalindicador',
            name='descount_value',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Indicador de Oferta'),
        ),
        migrations.AlterField(
            model_name='indicador',
            name='descount_value',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Indicador de Oferta'),
        ),
        migrations.DeleteModel(
            name='HistoricalCateroryProduct',
        ),
        migrations.AddField(
            model_name='historicalproduct',
            name='category_product',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='products.categoryproduct', verbose_name='Categoría del Producto'),
        ),
        migrations.AddField(
            model_name='product',
            name='category_product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.categoryproduct', verbose_name='Categoría del Producto'),
        ),
        migrations.AlterField(
            model_name='historicalindicador',
            name='category_product',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='products.categoryproduct', verbose_name='Categoría del Producto'),
        ),
        migrations.AlterField(
            model_name='indicador',
            name='category_product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.categoryproduct', verbose_name='Categoría del Producto'),
        ),
        migrations.DeleteModel(
            name='CateroryProduct',
        ),
    ]
