# Generated by Django 3.0.5 on 2020-05-21 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20200521_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='status',
            field=models.CharField(choices=[('False', 'False'), ('True', 'True')], max_length=10),
        ),
    ]
