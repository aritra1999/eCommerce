# Generated by Django 2.2.3 on 2019-11-03 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_placed'),
    ]

    operations = [
        migrations.AddField(
            model_name='placed',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]