from django.contrib import admin

# Register your models here.

from .models import Story, Word

admin.site.register(Story)
admin.site.register(Word)