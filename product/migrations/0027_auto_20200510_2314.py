# Generated by Django 3.0.5 on 2020-05-10 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0026_comment_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='comment/images/'),
        ),
    ]