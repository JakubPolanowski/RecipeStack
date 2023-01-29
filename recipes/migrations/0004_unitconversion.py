# Generated by Django 4.1.5 on 2023-01-29 04:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_recipe_ingredients'),
    ]

    operations = [
        migrations.CreateModel(
            name='UnitConversion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('factor', models.FloatField()),
                ('from_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_unit', to='recipes.unit')),
                ('to_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_unit', to='recipes.unit')),
            ],
        ),
    ]
