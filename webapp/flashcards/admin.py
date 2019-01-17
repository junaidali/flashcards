from django.contrib import admin

# Register your models here.
from .models import Category, Word

admin.site.register(Category)
admin.site.register(Word)