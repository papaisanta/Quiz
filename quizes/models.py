from django.db import models
from django.utils.text import slugify
import random

# Create your models here.

# Class model

class Class(models.Model):
    name = models.CharField(max_length=200)

    def __str__ (self):
        return str(self.name)

    def get_subjects(self):
        return self.subject_set.all()

# Subject model
class Subject(models.Model):
    classes = models.ForeignKey(Class, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=100, default="", blank=True)

    def __str__ (self):
        return f"{self.classes.name} - {self.name}"

    def get_chapters(self):
        return self.chapter_set.all()

    def save(self, *args, **kwargs):
        if not self.slug:
            slugified_class = slugify(self.classes.name)
            slugified_subject = slugify(self.name)
            self.slug = f"{slugified_class}-{slugified_subject}"
        super().save(*args, **kwargs)


# Chapter model

class Chapter(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    number_of_questions = models.IntegerField(default=20)
    required_score_to_pass = models.IntegerField(help_text='score in %', default=0)
    time = models.IntegerField(help_text='time in minutes', default=3)
    slug  = models.CharField(max_length=1000, blank=True)

    def __str__ (self):
        return f"{self.subject.classes.name} - {self.subject.name} - {self.name}"

    def save(self, *args, **kwargs):
        if not self.slug:
            chapter_slug = slugify(self.name)
            subject_slug = slugify(self.subject.name)
            class_slug = slugify(self.subject.classes.name)
            self.slug = f"{class_slug}-{subject_slug}-{chapter_slug}"
        super().save(*args, **kwargs)


    def get_questions(self):
        questions = list(self.question_set.all())
        random.shuffle(questions)
        return questions [: self.number_of_questions]