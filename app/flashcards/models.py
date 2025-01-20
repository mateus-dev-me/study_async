from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class FlashCard(models.Model):
    DIFFICULTY_CHOICES = (('D', 'Difícil'), ('M', 'Médio'), ('F', 'Fácil'))
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    question = models.CharField(max_length=100)
    response = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    difficulty = models.CharField(max_length=1, choices=DIFFICULTY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def css_challenge(self):
        if self.difficulty == 'F':
            return 'flashcard-facil'
        elif self.difficulty == 'M':
            return 'flashcard-medio'
        elif self.difficulty == 'D':
            return 'flashcard-dificil'

    def __str__(self):
        return self.question
