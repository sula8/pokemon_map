from django.db import models

class Pokemon(models.Model):
    title = models.CharField(max_length=200, verbose_name = "Имя")
    title_en = models.CharField(max_length=200, blank=True, verbose_name = "Имя по-английски")
    title_jp = models.CharField(max_length=200, blank=True, verbose_name = "Имя по-японски")
    images = models.ImageField(verbose_name = "Изображение")
    description = models.TextField(blank=True, verbose_name = "Описание")
    next_evolution = models.ForeignKey('self',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='previous_evolutions',
        verbose_name = "Эволюция")

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name='pokemon_entities', verbose_name = "Покемон")
    Lat = models.FloatField(verbose_name = "Широта")
    Lon = models.FloatField(verbose_name = "Долгота")
    appeared_at = models.DateTimeField(null=True, blank=True, verbose_name = "Появится в")
    disappeared_at = models.DateTimeField(null=True, blank=True, verbose_name = "Исчезнет в")
    level = models.IntegerField(null=True, blank=True, verbose_name = "Уровень")
    health = models.IntegerField(null=True, blank=True, verbose_name = "Здоровье")
    strength = models.IntegerField(null=True, blank=True, verbose_name = "Сила")
    defence = models.IntegerField(null=True, blank=True, verbose_name = "Защита")
    stamina = models.IntegerField(null=True, blank=True, verbose_name = "Выносливость")