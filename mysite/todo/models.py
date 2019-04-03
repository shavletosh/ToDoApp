from django.db import models
from django import forms


class TodoList(models.Model):
    clause = models.CharField(max_length=100)

    Activet = 'avtivet'
    Done = 'done'
    Canceled = 'canceled'

    Status = ((Activet, 'avtivet'),
    	(Done, 'done'),
    	(Canceled, 'canceled'))

    status = models.CharField(max_length=15, choices=Status, default=Activet)

    def __str__(self):
        return self.clause

