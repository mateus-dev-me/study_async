from django.contrib.auth.models import User
from django.db import models
from flashcards.models import Category, FlashCard


class FlashCardChallenge(models.Model):
    flashcard = models.ForeignKey(FlashCard, on_delete=models.DO_NOTHING)
    answered = models.BooleanField(default=False)
    got_it_right = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.flashcard.question


class Challenge(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=100)
    category = models.ManyToManyField(Category)
    number_questions = models.IntegerField()
    difficulty = models.CharField(
        max_length=1, choices=FlashCard.DIFFICULTY_CHOICES
    )

    flashcards = models.ManyToManyField(FlashCardChallenge)

    def __str__(self):
        return self.title
