# Generated by Django 3.0.5 on 2020-05-10 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0035_auto_20200511_0033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(blank=True, max_length=200),
        ),
    ]
