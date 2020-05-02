# Generated by Django 3.0.4 on 2020-04-13 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0030_recipeingredient_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mealplan',
            name='recipe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cookbook.Recipe'),
        ),
    ]
