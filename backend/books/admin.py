from django.contrib import admin

from .models import Book, ViewBook, Tag


admin.site.register(Book)
admin.site.register(ViewBook)
admin.site.register(Tag)
