# Generated by Django 3.0.7 on 2020-07-09 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UMS', '0002_userprofile_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, upload_to='users/images/'),
        ),
    ]
