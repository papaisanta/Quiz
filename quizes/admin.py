from django.contrib import admin
from .models import Class, Subject, Chapter

# Register your models here.

admin.site.register(Class)
admin.site.register(Subject)
admin.site.register(Chapter)