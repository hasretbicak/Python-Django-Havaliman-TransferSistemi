# Generated by Django 3.0.5 on 2020-05-23 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_auto_20200524_0053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='status',
            field=models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=10),
        ),
    ]
