# Generated by Django 2.0.1 on 2018-01-28 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickers', '0004_remove_ticker_coinmarketid'),
    ]

    operations = [
        migrations.CreateModel(
            name='TickerHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tickerId', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('symbol', models.CharField(max_length=255)),
                ('rank', models.IntegerField()),
                ('priceUsd', models.FloatField(blank=True, null=True)),
                ('priceBtc', models.FloatField(blank=True, null=True)),
                ('dayVolumeUsd', models.FloatField(blank=True, null=True)),
                ('markedCapUsd', models.FloatField(blank=True, null=True)),
                ('availableSupply', models.FloatField(blank=True, null=True)),
                ('totalSupply', models.FloatField(blank=True, null=True)),
                ('maxSupply', models.FloatField(blank=True, null=True)),
                ('percentChange1h', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('percentChange24h', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('percentChange7d', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('lastUpdated', models.DateTimeField()),
                ('dateAdded', models.DateTimeField()),
                ('lastAnalyzed', models.DateTimeField()),
            ],
        ),
    ]