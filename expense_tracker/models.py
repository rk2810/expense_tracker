from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Currency(models.Model):
    name = models.CharField(max_length=250)
    symbol = models.CharField(max_length=10)
    flag = models.IntegerField(default=1)

    def __str__(self):
        return self.name


class Expense(models.Model):
    EXPENSE_TYPE = (('Credit', 'credit'), ('Debit', 'debit'))
    title = models.CharField(max_length=250)
    payee = models.ForeignKey(User, on_delete=models.CASCADE)
    paid_to = models.CharField(max_length=250)
    amount = models.IntegerField()
    comment = models.TextField()
    currency = models.ForeignKey('Currency', on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    flag = models.CharField(max_length=10, choices=EXPENSE_TYPE, default='credit')

    class Meta:
        ordering = ('-created_at')

    def __str__(self):
        return self.title
