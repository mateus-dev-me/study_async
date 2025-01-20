from django.contrib import admin

from .models import Challenge, FlashCardChallenge

# Register your models here.
admin.site.register(FlashCardChallenge)
admin.site.register(Challenge)
