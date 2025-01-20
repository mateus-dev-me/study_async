from django.urls import path

from . import views

app_name = 'flashcards'
urlpatterns = [
    path('', views.home, name='home'),
    path(
        'remove_flashcard/<int:id>/',
        views.remove_flashcard,
        name='remove',
    ),
    path(
        'reply_flashcard/<int:id>/',
        views.reply_flashcard,
        name='reply',
    ),
]
