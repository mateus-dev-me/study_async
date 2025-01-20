from django.contrib import admin

from .models import Book, Tag, ViewBook

admin.site.register(Book)
admin.site.register(ViewBook)
admin.site.register(Tag)
