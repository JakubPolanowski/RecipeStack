# Generated by Django 4.1.5 on 2023-01-23 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_rename_foodgroups_foodgroup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodgroup',
            name='ingredients',
            field=models.ManyToManyField(blank=True, to='recipes.ingredient'),
        ),
    ]
