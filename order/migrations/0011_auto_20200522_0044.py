# Generated by Django 3.0.5 on 2020-05-21 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0010_auto_20200522_0022'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderproduct',
            name='tarih',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='orderproduct',
            name='vale',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]