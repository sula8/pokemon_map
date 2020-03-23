# Generated by Django 2.2.3 on 2020-03-23 23:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0017_auto_20200323_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='next_evolution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='previous_evolutions', to='pokemon_entities.Pokemon', verbose_name='Эволюция'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='Pokemon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pokemon_entities', to='pokemon_entities.Pokemon', verbose_name='Покемон'),
        ),
    ]