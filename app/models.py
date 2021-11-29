from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Todo(models.Model):
    status_choices = [
        ('p','pending'),
        ('c','completed')
    ]
    priority_choices = [
        ('1','one'),
        ('2','two'),
        ('3','three'),
        ('4','four'),
        ('5','five')
    ]
    title = models.CharField(max_length=50)
    status = models.CharField(max_length=2,choices=status_choices)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    priority = models.CharField(max_length=5,choices=priority_choices)
    created = models.DateTimeField(auto_now_add=True)
