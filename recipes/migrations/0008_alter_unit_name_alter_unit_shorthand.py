# Generated by Django 4.1.5 on 2023-01-29 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0007_unit_shorthand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='unit',
            name='shorthand',
            field=models.CharField(max_length=5, unique=True),
        ),
    ]
