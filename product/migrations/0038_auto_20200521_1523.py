# Generated by Django 3.0.5 on 2020-05-21 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0037_auto_20200521_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='yanıt',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='comment',
            name='yanıtlayan',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]