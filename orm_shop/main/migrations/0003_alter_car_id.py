# Generated by Django 4.2.7 on 2024-05-27 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_car_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
