# Generated by Django 2.2.3 on 2019-11-03 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20191103_1150'),
    ]

    operations = [
        migrations.AddField(
            model_name='placed',
            name='buyer_email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='placed',
            name='store_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
