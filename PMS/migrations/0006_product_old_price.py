# Generated by Django 3.0.7 on 2020-07-10 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PMS', '0005_auto_20200710_1009'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='old_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
    ]
