from django.urls import path

from . import views

app_name = 'books'
urlpatterns = [
    path('create_book/', views.create_book, name='create'),
    path('book/<int:id>/', views.book, name='detail'),
]
