# Generated by Django 2.0.1 on 2018-01-26 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tickerId', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('symbol', models.CharField(max_length=3)),
                ('rank', models.IntegerField()),
                ('priceUsd', models.FloatField()),
                ('priceBtc', models.FloatField()),
                ('dayVolumeUsd', models.FloatField()),
                ('markedCapUsd', models.FloatField()),
                ('availableSupply', models.FloatField()),
                ('totalSupply', models.FloatField()),
                ('maxSupply', models.FloatField()),
                ('percentChange1h', models.DecimalField(decimal_places=2, max_digits=5)),
                ('percentChange24h', models.DecimalField(decimal_places=2, max_digits=5)),
                ('percentChange7d', models.DecimalField(decimal_places=2, max_digits=5)),
                ('lastUpdated', models.DateTimeField()),
                ('dateAdded', models.DateTimeField()),
                ('lastAnalyzed', models.DateTimeField()),
            ],
        ),
    ]
