# Generated by Django 3.0.5 on 2020-04-21 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_auto_20200421_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.CharField(max_length=200),
        ),
    ]
