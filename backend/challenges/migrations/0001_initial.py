# Generated by Django 5.0.1 on 2024-01-28 18:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("flashcards", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="FlashCardChallenge",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("answered", models.BooleanField(default=False)),
                ("got_it_right", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "flashcard",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="flashcards.flashcard",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Challenge",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("number_questions", models.IntegerField()),
                (
                    "difficulty",
                    models.CharField(
                        choices=[("D", "Difícil"), ("M", "Médio"), ("F", "Fácil")],
                        max_length=1,
                    ),
                ),
                ("category", models.ManyToManyField(to="flashcards.category")),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "flashcards",
                    models.ManyToManyField(to="challenges.flashcardchallenge"),
                ),
            ],
        ),
    ]
