# Generated by Django 3.0.5 on 2020-05-21 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20200521_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='status',
            field=models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=10),
        ),
    ]