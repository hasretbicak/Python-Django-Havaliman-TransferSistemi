# Generated by Django 3.0.5 on 2020-04-21 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0014_auto_20200421_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(blank=True, max_length=200),
        ),
    ]