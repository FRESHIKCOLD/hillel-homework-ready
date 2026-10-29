from django.db import models
from django.core.validators import MinValueValidator


class Card(models.Model):
    name = models.CharField(max_length=150, verbose_name="Назва")
    game = models.CharField(max_length=80, default="Magic: The Gathering", verbose_name="Гра")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Кількість")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0,
                                validators=[MinValueValidator(0)], verbose_name="Ціна")
    description = models.TextField(blank=True, verbose_name="Опис")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = "Картка"
        verbose_name_plural = "Картки"
