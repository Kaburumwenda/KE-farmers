# Generated by Django 3.0.7 on 2020-07-16 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PMS', '0008_product_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorylang',
            name='lang',
            field=models.CharField(choices=[('en', 'English'), ('tr', 'Turkish'), ('fr', 'French'), ('ar', 'Arabic'), ('sw', 'Swahili'), ('kik', 'Kimîîru')], max_length=6),
        ),
        migrations.AlterField(
            model_name='productlang',
            name='lang',
            field=models.CharField(choices=[('en', 'English'), ('tr', 'Turkish'), ('fr', 'French'), ('ar', 'Arabic'), ('sw', 'Swahili'), ('kik', 'Kimîîru')], max_length=6),
        ),
    ]
