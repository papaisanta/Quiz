from django.contrib import admin
from .models import Question, Answer

# Register your models here.

class AnswerInlines(admin.TabularInline):
    model = Answer

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInlines]

admin.site.register(Question, QuestionAdmin)