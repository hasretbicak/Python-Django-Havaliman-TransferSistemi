# Generated by Django 3.0.5 on 2020-04-15 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_setting_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='bground',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
