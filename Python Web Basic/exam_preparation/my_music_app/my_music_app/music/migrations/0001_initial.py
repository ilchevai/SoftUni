# Generated by Django 4.2.2 on 2023-06-23 09:51

import django.core.validators
from django.db import migrations, models
import my_music_app.music.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('artist', models.CharField(max_length=30)),
                ('genre', models.CharField(choices=[('PopMusic', 'PopMusic'), ('JazzMusic', 'JazzMusic'), ('R&BMusic', 'R&BMusic'), ('RockMusic', 'RockMusic'), ('Country Music', 'Country Music'), ('Dance Music', 'Dance Music'), ('Hip Hop Music', 'Hip Hop Music'), ('Other', 'Other')], max_length=30)),
                ('descriptions', models.TextField(blank=True, null=True)),
                ('image_url', models.URLField()),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)])),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(validators=[django.core.validators.MinLengthValidator(2), django.core.validators.MaxLengthValidator(15), my_music_app.music.validators.LetterNumberUnderscoreValidator()])),
                ('email', models.EmailField(max_length=254)),
                ('age', models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
    ]
