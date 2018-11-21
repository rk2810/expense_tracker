from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta, datetime


class Currency(models.Model):
    name = models.CharField(max_length=250)
    symbol = models.CharField(max_length=10)
    flag = models.IntegerField(default=1)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=250)
    icon = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    public = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.name


class UserCategory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)


class Account(models.Model):
    COLORS_AVAILABLE = (('Red', 'red'), ('Blue', 'blue'), ('Green', 'green'))
    color = models.CharField(max_length=10, choices=COLORS_AVAILABLE, default='Red')
    description = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    public = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created_at',)


class UserAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account = models.ForeignKey('Account', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)


class Transaction(models.Model):
    EXPENSE_TYPE = (('Credit', 'credit'), ('Debit', 'debit'), ('Other', 'other'))
    title = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField()
    comment = models.TextField()
    account = models.ForeignKey('Account', on_delete=models.PROTECT)
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    currency = models.ForeignKey('Currency', on_delete=models.SET_NULL, null=True)
    date_time = models.DateTimeField(default=datetime.now() + timedelta(hours=5, minutes=30))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    flag = models.CharField(max_length=10, choices=EXPENSE_TYPE, default='Credit')

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title
