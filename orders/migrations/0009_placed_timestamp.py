# Generated by Django 2.2.3 on 2019-11-28 14:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_auto_20191103_1256'),
    ]

    operations = [
        migrations.AddField(
            model_name='placed',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
