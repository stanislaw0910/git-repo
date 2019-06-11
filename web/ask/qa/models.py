from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class QuestionManager(models.Manager):
    def popular(self):
        return self.order_by('-rating')
    def new(self):
        return self.order_by('-added_at')


class Question(models.Model):
    title = models.CharField(default='', max_length=255)
    text = models.TextField(default='')
    added_at = models.DateField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    likes = models.ManyToManyField(User, related_name='q_likes' )
    objects = QuestionManager()


class Answer(models.Model):
    text = models.TextField(default='')
    added_at = models.DateField(auto_now_add=True)
    question = models.ForeignKey(Question, null=True, on_delete=models.SET_NULL)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
