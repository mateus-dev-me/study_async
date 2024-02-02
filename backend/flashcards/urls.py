from django.urls import path

from . import views

urlpatterns = [
    path('new_flashcard/', views.create_flashcard, name='new_flashcard'),
    path(
        'remove_flashcard/<int:id>/',
        views.remove_flashcard,
        name='remove_flashcard',
    ),
    path(
        'reply_flashcard/<int:id>/',
        views.reply_flashcard,
        name='reply_flashcard',
    ),
]
