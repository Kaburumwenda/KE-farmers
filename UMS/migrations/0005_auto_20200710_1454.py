# Generated by Django 3.0.7 on 2020-07-10 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('currencies', '0006_increase_name_max_length'),
        ('HOME', '0006_auto_20200710_1448'),
        ('UMS', '0004_auto_20200710_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='currency',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='currencies.Currency'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='HOME.Language'),
        ),
    ]
