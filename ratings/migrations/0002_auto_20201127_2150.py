# Generated by Django 3.1.3 on 2020-11-27 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='contact',
            field=models.PositiveIntegerField(blank=True, default='2547123456'),
        ),
    ]