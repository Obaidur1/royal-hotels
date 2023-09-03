# Generated by Django 4.2.4 on 2023-09-03 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='royalhotelmodel',
            options={'verbose_name_plural': "Royal Hotel's"},
        ),
        migrations.AlterModelOptions(
            name='user_reviews',
            options={'verbose_name_plural': 'Reviews'},
        ),
        migrations.AddField(
            model_name='royalhotelmodel',
            name='cost_per_day',
            field=models.DecimalField(decimal_places=2, default=500, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='royalhotelmodel',
            name='photos',
            field=models.ImageField(blank=True, null=True, upload_to='static/photos/'),
        ),
    ]
