from django.contrib import admin
from expense_tracker.models import Transaction, Currency, Category, Account

admin.site.register(Transaction)
admin.site.register(Currency)
admin.site.register(Category)
admin.site.register(Account)
