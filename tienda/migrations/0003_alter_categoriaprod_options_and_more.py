# Generated by Django 4.2.1 on 2023-08-13 04:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0002_producto_create_producto_update'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoriaprod',
            options={'verbose_name': 'categoriaproducto', 'verbose_name_plural': 'categoriaproductos'},
        ),
        migrations.AlterModelTable(
            name='categoriaprod',
            table='Categorias',
        ),
    ]
