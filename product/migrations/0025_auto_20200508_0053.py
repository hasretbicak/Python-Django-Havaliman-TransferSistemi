# Generated by Django 3.0.5 on 2020-05-07 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0024_auto_20200508_0015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
