from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.messages import constants
from django.shortcuts import redirect, render

from .models import Book, Tag, ViewBook


@login_required
def create_book(request):
    if request.method == 'GET':
        books = Book.objects.filter(user=request.user)
        total_views = ViewBook.objects.filter(book__user=request.user).count()

        tags = Tag.objects.all()

        filter_tags = request.GET.get('tags')
        if filter_tags:
            books = books.filter(tags=filter_tags)

        return render(
            request,
            'create_book.html',
            {'books': books, 'views': total_views, 'tags': tags},
        )
    elif request.method == 'POST':
        title = request.POST.get('title')
        tags = request.POST.get('tags')
        file = request.FILES.get('file')

        if len(title.strip()) == 0:
            messages.add_message(
                request,
                constants.ERROR,
                'Preencha o título da apostila por favor.',
            )
            return redirect('/books/create_book')

        book = Book(
            user=request.user,
            title=title,
            file=file,
        )
        book.save()
        book.tags.add(tags)
        book.save()
        messages.add_message(
            request,
            constants.SUCCESS,
            'Apostila adicionada com sucesso!',
        )
        return redirect('/books/create_book')


@login_required
def book(request, id):
    book = Book.objects.get(id=id)
    view = ViewBook(ip=request.META.get('REMOTE_ADDR'), book=book)
    view.save()
    unique_views = (
        ViewBook.objects.filter(book=book).values('ip').distinct().count()
    )
    total_views = ViewBook.objects.filter(book=book).count()
    return render(
        request,
        'book.html',
        {
            'book': book,
            'unique_views': unique_views,
            'total_views': total_views,
        },
    )
