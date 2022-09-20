# Generated by Django 4.1.1 on 2022-09-20 12:03

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipes', '0002_alter_ingredientinrecipe_ingredient_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Favorites',
            new_name='Favorite',
        ),
        migrations.AlterModelOptions(
            name='ingredientinrecipe',
            options={'verbose_name': 'Ингредиент в рецепте', 'verbose_name_plural': 'Ингредиенты в рецепте'},
        ),
        migrations.AlterField(
            model_name='ingredientinrecipe',
            name='amount',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1, message='Минимальное количество 1!')], verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='ingredientinrecipe',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredient_list', to='recipes.recipe', verbose_name='Рецепт'),
        ),
    ]
