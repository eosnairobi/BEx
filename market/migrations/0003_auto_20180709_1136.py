# Generated by Django 2.0.7 on 2018-07-09 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_auto_20180709_1057'),
    ]

    operations = [
        migrations.AddField(
            model_name='pricelisting',
            name='circulating_supply',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=100),
        ),
        migrations.AddField(
            model_name='pricelisting',
            name='max_supply',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=100),
        ),
        migrations.AddField(
            model_name='pricelisting',
            name='percent_change_1h',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pricelisting',
            name='percent_change_24h',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pricelisting',
            name='percent_change_7d',
            field=models.IntegerField(default=0),
        ),
    ]
