# Generated by Django 2.0.1 on 2018-01-26 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticker',
            name='availableSupply',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ticker',
            name='dayVolumeUsd',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ticker',
            name='markedCapUsd',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ticker',
            name='maxSupply',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ticker',
            name='percentChange1h',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='ticker',
            name='percentChange24h',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='ticker',
            name='percentChange7d',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='ticker',
            name='priceBtc',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ticker',
            name='priceUsd',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ticker',
            name='symbol',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='ticker',
            name='totalSupply',
            field=models.FloatField(blank=True, null=True),
        ),
    ]