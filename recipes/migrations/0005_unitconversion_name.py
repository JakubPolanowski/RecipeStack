# Generated by Django 4.1.5 on 2023-01-29 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_unitconversion'),
    ]

    operations = [
        migrations.AddField(
            model_name='unitconversion',
            name='name',
            field=models.CharField(default='temp', max_length=15, unique=True),
            preserve_default=False,
        ),
    ]
