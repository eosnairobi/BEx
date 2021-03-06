# Generated by Django 2.0.7 on 2018-07-09 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0005_auto_20180709_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricelisting',
            name='circulating_supply',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=100, null=True),
        ),
        migrations.AlterField(
            model_name='pricelisting',
            name='daily_volume',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='pricelisting',
            name='market_cap',
            field=models.DecimalField(decimal_places=1, max_digits=100, null=True),
        ),
        migrations.AlterField(
            model_name='pricelisting',
            name='max_supply',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=100, null=True),
        ),
        migrations.AlterField(
            model_name='pricelisting',
            name='percent_change_1h',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='pricelisting',
            name='percent_change_24h',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='pricelisting',
            name='percent_change_7d',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='pricelisting',
            name='usd',
            field=models.DecimalField(decimal_places=4, max_digits=100, null=True),
        ),
    ]
