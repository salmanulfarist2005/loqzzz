# Generated by Django 5.0.2 on 2024-03-05 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_dealershipinterest_dealership'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='position',
            field=models.CharField(max_length=200),
        ),
    ]
