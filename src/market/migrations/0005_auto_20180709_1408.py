# Generated by Django 2.0.7 on 2018-07-09 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0004_auto_20180709_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricelisting',
            name='btc',
            field=models.DecimalField(decimal_places=10, max_digits=100, null=True),
        ),
    ]