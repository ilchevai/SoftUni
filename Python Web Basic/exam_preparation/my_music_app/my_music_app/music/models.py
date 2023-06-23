from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator

from my_music_app.music.validators import LetterNumberUnderscoreValidator


# Create your models here.
class Profile(models.Model):
    username = models.CharField(
        blank=False,
        null=False,
        validators=(
            MinLengthValidator(2),
            MaxLengthValidator(15),
            LetterNumberUnderscoreValidator()
        )
    )
    email = models.EmailField(
        blank=False, null=False
    )
    age = models.PositiveIntegerField(
        blank=True, null=True
    )

    def __str__(self):
        return self.username


class Album(models.Model):
    GENRE_CHOICES = (
        ("pop", "PopMusic"),
        ("jazz", "JazzMusic"),
        ("r_b", "R&BMusic"),
        ("rock", "RockMusic"),
        ("country", "Country Music"),
        ("dance", "Dance Music"),
        ("hip_hop", "Hip Hop Music"),
        ("other", "Other")
    )

    name = models.CharField(
        blank=False, null=False,
        max_length=30,
        unique=True
    )
    artist = models.CharField(
        blank=False, null=False,
        max_length=30
    )
    genre = models.CharField(
        blank=False, null=False,
        max_length=30,
        choices=GENRE_CHOICES
    )
    descriptions = models.TextField(
        blank=True, null=True
    )
    image_url = models.URLField(
        blank=False, null=False
    )
    price = models.FloatField(
        blank=False, null=False,
        validators=(MinValueValidator(0.0),)
    )
