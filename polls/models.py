import datetime
from django.db import models
from django.utils import timezone


class Question(models.Model):
    english_question_text = models.CharField(max_length=200)
    amharic_question_text = models.CharField(max_length=200, blank=True)
    oromic_question_text = models.CharField(max_length=200, blank=True)
    pub_date = models.DateTimeField('date published')
    dead_line = models.DateTimeField('deadline')

    def __str__(self):
        return self.english_question_text

    def was_published_recently(self):
        return  timezone.now() >= self.pub_date >= timezone.now() - datetime.timedelta(days=1)



class Choice(models.Model):
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    english_choice_text = models.CharField(max_length=200)
    amharic_choice_text = models.CharField(max_length=200, blank=True)
    oromic_choice_text = models.CharField(max_length=200 , blank=True)

    def __str__(self):
        return self.english_choice_text


class Citizen(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    voter_id = models.CharField(max_length=20, unique=True, help_text='Provide a unique voter id to use each time you vote. Keep it in secret and do not forget the voter id!')
    voted_questions = models.ManyToManyField(Question, blank=True)

    def __str__(self):
        return ' '.join([self.first_name, self.last_name])