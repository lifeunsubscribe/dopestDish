# Generated by Django 3.1.3 on 2020-12-03 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_auto_20201203_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.PositiveIntegerField(choices=[(1, '1 star'), (2, '2 stars'), (3, '3 stars'), (4, '4 stars'), (5, '5 stars')]),
        ),
    ]
