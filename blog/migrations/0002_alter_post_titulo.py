# Generated by Django 4.2.1 on 2023-08-11 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='titulo',
            field=models.CharField(max_length=50, verbose_name='Titulo del Post'),
        ),
    ]