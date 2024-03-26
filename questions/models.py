from django.db import models
from quizes.models import Chapter

# Create your models here.

class Question(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    text = models.CharField(max_length=100000)
    
    def __str__ (self):
        return str(self.text)

    def get_answers(self):
        return self.answer_set.all()

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=10000)
    correct = models.BooleanField(default=False)

    def __str__ (self):
        return f"Question: {self.question.text}, Answer: {self.text}, is_correct: {self.correct}"