# Generated by Django 2.2.3 on 2019-10-03 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20191003_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='shipping_total',
            field=models.DecimalField(decimal_places=2, default=50.0, max_digits=100),
        ),
    ]
