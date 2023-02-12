from django.db import models
from django.contrib.auth.models import User
import django.utils.datetime_safe
from django.db import migrations, models
from datetime import datetime



# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

# class Vote(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
#     voted_at = models.DateTimeField(auto_now_add=True)

class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    poll = models.ForeignKey(Question, on_delete=models.CASCADE)
    option = models.ForeignKey(Choice, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=datetime.now, null=True, blank=True)

    def __str__(self):
        return f"{self.user} selected {self.option.choice_text} at {self.timestamp}"
