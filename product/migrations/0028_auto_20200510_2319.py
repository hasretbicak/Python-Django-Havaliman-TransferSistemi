# Generated by Django 3.0.5 on 2020-05-10 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0027_auto_20200510_2314'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='image',
        ),
        migrations.AddField(
            model_name='comment',
            name='image_com',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
