# Generated by Django 3.1.7 on 2021-02-23 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0011_auto_20210222_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='health.location'),
        ),
    ]
