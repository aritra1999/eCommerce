# Generated by Django 2.2.3 on 2019-11-28 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_placed_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='placed',
            name='order_id',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]