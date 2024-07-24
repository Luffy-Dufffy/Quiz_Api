from django.db import models

# Create your models here.


class Questions(models.Model):
    question = models.TextField()
    category = models.TextField()
    level = models.TextField()


class Options(models.Model):
    option = models.TextField()
    isCorrect = models.BooleanField(False)
    question_id = models.ForeignKey(Questions, on_delete=models.CASCADE)