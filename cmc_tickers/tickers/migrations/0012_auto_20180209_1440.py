# Generated by Django 2.0.1 on 2018-02-09 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickers', '0011_auto_20180209_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticker',
            name='btcPercentChange1h',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ticker',
            name='btcPercentChange24h',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ticker',
            name='btcPercentChange7d',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tickerhistory',
            name='btcPercentChange1h',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tickerhistory',
            name='btcPercentChange24h',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tickerhistory',
            name='btcPercentChange7d',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
