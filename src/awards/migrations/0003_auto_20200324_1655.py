# Generated by Django 3.0.4 on 2020-03-24 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0002_auto_20200324_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='award',
            name='img',
            field=models.ImageField(upload_to='images'),
        ),
    ]
