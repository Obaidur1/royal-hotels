# Generated by Django 4.2.4 on 2023-09-08 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_royalhotelmodel_average_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='royalhotelmodel',
            name='average_rating',
            field=models.IntegerField(default=0, max_length=1),
        ),
    ]
