# Generated by Django 4.2.4 on 2023-09-07 12:04

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0002_alter_royalhotelmodel_options_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='user_reviews',
            unique_together={('hotel', 'user')},
        ),
    ]