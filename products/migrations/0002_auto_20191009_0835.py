# Generated by Django 2.2.3 on 2019-10-09 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='product',
            name='seller',
            field=models.CharField(default='admin', max_length=120),
        ),
    ]