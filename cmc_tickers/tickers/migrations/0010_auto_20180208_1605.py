# Generated by Django 2.0.1 on 2018-02-08 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickers', '0009_auto_20180205_1311'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticker',
            name='dayVolumeBtcVariation',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tickerhistory',
            name='dayVolumeBtcVariation',
            field=models.FloatField(blank=True, null=True),
        ),
    ]