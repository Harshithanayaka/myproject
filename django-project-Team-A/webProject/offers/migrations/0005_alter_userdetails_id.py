# Generated by Django 4.0 on 2022-07-09 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0004_dongle_postpaid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]