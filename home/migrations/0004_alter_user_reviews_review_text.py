# Generated by Django 4.2.4 on 2023-09-07 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_user_reviews_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_reviews',
            name='review_text',
            field=models.TextField(max_length=50),
        ),
    ]
