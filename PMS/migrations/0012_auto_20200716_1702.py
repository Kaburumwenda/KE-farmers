# Generated by Django 3.0.7 on 2020-07-16 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PMS', '0011_auto_20200716_1654'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Brand',
            new_name='brand',
        ),
        migrations.AddField(
            model_name='product',
            name='seller',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
